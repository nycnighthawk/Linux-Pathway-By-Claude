---
{"title": "debhelper(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/debhelper.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# debhelper(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DEBHELPER COMMANDS](#DEBHELPER_COMMANDS) \| [DEBHELPER CONFIG FILES](#DEBHELPER_CONFIG_FILES) \| [SHARED DEBHELPER OPTIONS](#SHARED_DEBHELPER_OPTIONS) \| [COMMON DEBHELPER OPTIONS](#COMMON_DEBHELPER_OPTIONS) \| [BUILD SYSTEM OPTIONS](#BUILD_SYSTEM_OPTIONS) \| [COMPATIBILITY LEVELS](#COMPATIBILITY_LEVELS) \| [NOTES](#NOTES) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    debhelper(7)                    Debhelper                    debhelper(7)

## [](#NAME)NAME

           debhelper - the debhelper tool suite

## [](#SYNOPSIS)SYNOPSIS

           dh_* [-v] [-a] [-i] [--no-act] [-ppackage] [-Npackage] [-Ptmpdir]

## [](#DESCRIPTION)DESCRIPTION

           Debhelper is used to help you build a Debian package. The
           philosophy behind debhelper is to provide a collection of small,
           simple, and easily understood tools that are used in debian/rules
           to automate various common aspects of building a package. This
           means less work for you, the packager.  It also, to some degree
           means that these tools can be changed if Debian policy changes,
           and packages that use them will require only a rebuild to comply
           with the new policy.

           A typical debian/rules file that uses debhelper will call several
           debhelper commands in sequence, or use dh(1) to automate this
           process. Examples of rules files that use debhelper are in
           /usr/share/doc/debhelper/examples/

           To create a new Debian package using debhelper, you can just copy
           one of the sample rules files and edit it by hand. Or you can try
           the dh-make package, which contains a dh_make command that
           partially automates the process. For a more gentle introduction,
           the maint-guide Debian package contains a tutorial about making
           your first package using debhelper.

           Except where the tool explicitly denotes otherwise, all of the
           debhelper tools assume that they run from the root directory of an
           unpacked source package.  This is so they can locate files like
           debian/control when needed.

## [](#DEBHELPER_COMMANDS)DEBHELPER COMMANDS

           Here is the list of debhelper commands you can use. See their man
           pages for additional documentation.

           dh_assistant(1)
               tool for supporting debhelper tools and provide introspection

           dh_auto_build(1)
               automatically builds a package

           dh_auto_clean(1)
               automatically cleans up after a build

           dh_auto_configure(1)
               automatically configure a package prior to building

           dh_auto_install(1)
               automatically runs make install or similar

           dh_auto_test(1)
               automatically runs a package's test suites

           dh_bugfiles(1)
               install bug reporting customization files into package build
               directories

           dh_builddeb(1)
               build Debian binary packages

           dh_clean(1)
               clean up package build directories

           dh_compress(1)
               compress files and fix symlinks in package build directories

           dh_computeautosubstvars(1)
               compute substvars relevant to most packages

           dh_dwz(1)
               optimize DWARF debug information in ELF binaries via dwz

           dh_fixperms(1)
               fix permissions of files in package build directories

           dh_gencontrol(1)
               generate and install control file

           dh_icons(1)
               Update caches of Freedesktop icons

           dh_install(1)
               install files into package build directories

           dh_installalternatives(1)
               install declarative alternative rules

           dh_installcatalogs(1)
               install and register SGML Catalogs

           dh_installchangelogs(1)
               install changelogs into package build directories

           dh_installcron(1)
               install cron scripts into etc/cron.*

           dh_installdeb(1)
               install files into the DEBIAN directory

           dh_installdebconf(1)
               install files used by debconf in package build directories

           dh_installdirs(1)
               create subdirectories in package build directories

           dh_installdocs(1)
               install documentation into package build directories

           dh_installemacsen(1)
               register an Emacs add on package

           dh_installexamples(1)
               install example files into package build directories

           dh_installgsettings(1)
               install GSettings overrides and set dependencies

           dh_installifupdown(1)
               install if-up and if-down hooks

           dh_installinfo(1)
               install info files

           dh_installinit(1)
               install service init files into package build directories

           dh_installinitramfs(1)
               install initramfs hooks and setup maintscripts

           dh_installlogcheck(1)
               install logcheck rulefiles into etc/logcheck/

           dh_installlogrotate(1)
               install logrotate config files

           dh_installman(1)
               install man pages into package build directories

           dh_installmenu(1)
               install Debian menu files into package build directories

           dh_installmime(1)
               install mime files into package build directories

           dh_installmodules(1)
               register kernel modules

           dh_installpam(1)
               install pam support files

           dh_installppp(1)
               install ppp ip-up and ip-down files

           dh_installsystemd(1)
               install systemd unit files

           dh_installsystemduser(1)
               install systemd unit files

           dh_installsysusers(1)
               install and integrates systemd sysusers files

           dh_installtmpfiles(1)
               install tmpfiles.d configuration files

           dh_installudev(1)
               install udev rules files

           dh_installwm(1)
               register a window manager

           dh_installxfonts(1)
               register X fonts

           dh_link(1)
               create symlinks in package build directories

           dh_lintian(1)
               install lintian override files into package build directories

           dh_listpackages(1)
               list binary packages debhelper will act on

           dh_makeshlibs(1)
               automatically create shlibs file and call dpkg-gensymbols

           dh_md5sums(1)
               generate DEBIAN/md5sums file

           dh_missing(1)
               check for missing files

           dh_movefiles(1)
               move files out of debian/tmp into subpackages

           dh_movetousr(1)
               canonicalize location according to merged-/usr

           dh_perl(1)
               calculates Perl dependencies and cleans up after MakeMaker

           dh_prep(1)
               perform cleanups in preparation for building a binary package

           dh_shlibdeps(1)
               calculate shared library dependencies

           dh_strip(1)
               strip executables, shared libraries, and some static libraries

           dh_systemd_enable(1)
               enable/disable systemd unit files

           dh_systemd_start(1)
               start/stop/restart systemd unit files

           dh_testdir(1)
               test directory before building Debian package

           dh_testroot(1)
               ensure that a package is built with necessary level of root
               permissions

           dh_ucf(1)
               register configuration files with ucf

           dh_update_autotools_config(1)
               Update autotools config files

           dh_usrlocal(1)
               migrate usr/local directories to maintainer scripts

       Deprecated Commands
           A few debhelper commands are deprecated and should not be used.

           dh_installmanpages(1)
               old-style man page installer (deprecated)

       Other Commands
           If a program's name starts with dh_, and the program is not on the
           above lists, then it is not part of the debhelper package, but it
           should still work like the other programs described on this page.

## [](#DEBHELPER_CONFIG_FILES)DEBHELPER CONFIG FILES

           Many debhelper commands make use of files in debian/ to control
           what they do. Besides the common debian/changelog and
           debian/control, which are in all packages, not just those using
           debhelper, some additional files can be used to configure the
           behavior of specific debhelper commands. These files are typically
           named debian/package.foo (where package of course, is replaced
           with the package that is being acted on).

           For example, dh_installdocs uses files named debian/package.docs
           to list the documentation files it will install. See the man pages
           of individual commands for details about the names and formats of
           the files they use.  Generally, these files will list files to act
           on, one file per line. Some programs in debhelper use pairs of
           files and destinations or slightly more complicated formats.

           Note if there is only one binary package listed in debian/control,
           then debhelper will use debian/foo when there's no
           debian/package.foo file.  In compat levels before compat 15, this
           fallback also occurs for the first binary package listed in
           debian/control when there are multiple binary packages. However,
           it is often a good idea to keep the package. prefix as it is more
           explicit and also required when upgrading to compat 15.

           Additionally, there are some special cases where debhelper will
           always fallback to a prefix-less version.  These are cases such as
           debian/copyright and debian/changelog, where the files are
           generally used and needed for all binary packages.

           In some rare cases, you may want to have different versions of
           these files for different architectures or OSes. If files named
           debian/package.foo.ARCH or debian/package.foo.OS exist, where ARCH
           and OS are the same as the output of "dpkg-architecture
           -qDEB_HOST_ARCH" / "dpkg-architecture -qDEB_HOST_ARCH_OS", then
           they will be used in preference to other, more general files.

           Mostly, these config files are used to specify lists of various
           types of files. Documentation or example files to install, files
           to move, and so on.  When appropriate, in cases like these, you
           can use standard shell wildcard characters (? and * and [..]
           character classes) in the files.  You can also put comments in
           these files; lines beginning with # are ignored.

           The syntax of these files is intentionally kept very simple to
           make them easy to read, understand, and modify.

       Substitutions in debhelper config files
           In compatibility level 13 and later, it is possible to use simple
           substitutions in debhelper config files for the following tools:

           •   dh_clean

           •   dh_install

           •   dh_installcatalogs

           •   dh_installdeb

           •   dh_installdirs

           •   dh_installdocs

           •   dh_installexamples

           •   dh_installinfo

           •   dh_installman

           •   dh_installwm

           •   dh_link

           •   dh_missing

           •   dh_ucf

           All substitution variables are of the form ${foo} and the braces
           are mandatory.  Variable names are case-sensitive and consist of
           alphanumerics (a-zA-Z0-9), hyphens (-), underscores (_), and
           colons (:).  The first character must be an alphanumeric.

           If you need a literal dollar sign that cannot trigger a
           substitution, you can either use the ${Dollar} substitution or the
           sequence ${}.

           The following expansions are available:

           DEB_HOST_*, DEB_BUILD_*, DEB_TARGET_*
               Expands to the relevant dpkg-architecture(1) value (similar to
               dpkg-architecture -qVARIABLE_HERE).

               When in doubt, the DEB_HOST_* variant is the one that will
               work both for native and cross builds.

               For performance reasons, debhelper will attempt to resolve
               these names from the environment first before consulting
               dpkg-architecture(1).  This is mostly mentioned for
               completeness as it will not matter for most cases.

           Dollar
               Expands to a single literal $-symbol.  This symbol will never
               be considered part of a substitution variable.  That is:

                  # Triggers an error
                  ${NO_SUCH_TOKEN}
                  # Expands to the literal value "${NO_SUCH_TOKEN}"
                  ${Dollar}{NO_SUCH_TOKEN}

               This variable equivalent to the sequence ${} and the two can
               be used interchangeably.

           Newline, Space, Tab
               Expands to a single ASCII newline, space and tab respectively.

               This can be useful if you need to include a literal whitespace
               character (e.g. space) where it would otherwise be stripped or
               used as a separator.

           [1menv:NAME
               Expands to the environment variable NAME.  The environment
               variable must be set (but can be set to the empty string).

           Note that all variables must expand to a defined value.  As an
           example, if debhelper sees ${env:FOO}, then it will insist that
           the environment variable FOO is set (it can be set to the empty
           string).

           Substitution limits

           To avoid infinite loops and resource exhaustion, debhelper will
           stop with an error if the token contains many substitution
           variables (50) or the total size of the expanded value exceed a
           certain size (4096 characters or 3x length of the original input -
           whichever is bigger).

           Note the limit is per token. Every helper decides its own
           definition of a token. The common case of files like
           debian/package.install, each token is a file/path name.

           Substitution limitations: filtering

           The built-in substitution cannot be used to "filter" out content.
           Attempts to create "comments" or "empty lines" via substitution
           will result in those variables being considered a token in its own
           right with the content given.

           If you want filtering, consider using an executable debhelper
           config file with dh-exec as interpreter. The dh-exec tool supports
           several features out of the box. Though keep in mind that dh-exec
           has its own substitution logic that can feature interact with the
           one from debhelper.

       Executable debhelper config files
           If you need additional flexibility, many of the debhelper tools
           (e.g. dh_install(1)) support executing a config file as a script.

           To use this feature, simply mark the config file as executable
           (e.g. chmod +x debian/package.install) and the tool will attempt
           to execute it and use the output of the script.  In many cases,
           you can use dh-exec(1) as interpreter of the config file to retain
           most of the original syntax while getting the additional
           flexibility you need.

           When using executable debhelper config files, please be aware of
           the following:

           •   The executable config file must exit with success (i.e. its
               return code should indicate success).

           •   In compatibility level 13+, the output will be subject to
               substitutions (see "Substitutions in debhelper config files")
               where the tool support these.  Remember to be careful if your
               generator also provides substitutions as this can cause
               unnecessary confusion. Notably, the commonly used dh-exec tool
               has its own substitution support.

               Otherwise, the output will be used exactly as-is.  Notably,
               debhelper will not expand wildcards or strip comments or strip
               whitespace in the output it reads. The dh-exec tool has an
               output filter on by default that will prune these things out.

           If you need the package to build on a file system where you cannot
           disable the executable bit, then you can use dh-exec(1) and its
           strip-output script.

## [](#SHARED_DEBHELPER_OPTIONS)SHARED DEBHELPER OPTIONS

           The following command line options are supported by all debhelper
           programs.

           -v, --verbose
               Verbose mode: show commands that modify the package build
               directory.

               Note that verbose mode may also output other "internal"
               commands that do not directly affect the package build
               directory.

           --no-act
               Do not really do anything. If used with -v, the result is that
               the command will output what it would have done.

           -a, --arch
               Act on architecture dependent packages that should be built
               for the DEB_HOST_ARCH architecture.

           -i, --indep
               Act on all architecture independent packages.

           -ppackage, --package=package
               Act on the package named package. This option may be specified
               multiple times to make debhelper operate on a given set of
               packages.

           -s, --same-arch
               Deprecated alias of -a.

               This option is removed in compat 12.

           -Npackage, --no-package=package
               Do not act on the specified package even if an -a, -i, or -p
               option lists the package as one that should be acted on.

           --remaining-packages
               Do not act on the packages which have already been acted on by
               this debhelper command earlier (i.e. if the command is present
               in the package debhelper log).  For example, if you need to
               call the command with special options only for a couple of
               binary packages, pass this option to the last call of the
               command to process the rest of packages with default settings.

           -Ptmpdir, --tmpdir=tmpdir
               Use tmpdir for package build directory. The default is
               debian/package

           --mainpackage=package
               Deprecated: This option has no practical use in compat 15 or
               later as the behaviour it affects is removed in compat 15.

               This little-used option changes the package which debhelper
               considers the "main package", that is, the first one listed in
               debian/control, and the one for which debian/foo files can be
               used instead of the usual debian/package.foo files.

           -O=option|bundle
               This is used by dh(1) when passing user-specified options to
               all the commands it runs. If the command supports the
               specified option or option bundle, it will take effect. If the
               command does not support the option (or any part of an option
               bundle), it will be ignored.

## [](#COMMON_DEBHELPER_OPTIONS)COMMON DEBHELPER OPTIONS

           The following command line options are supported by some debhelper
           programs.  See the man page of each program for a complete
           explanation of what each option does.

           -n  Do not modify postinst, postrm, etc. scripts.

           -Xitem, --exclude=item
               Exclude an item from processing. This option may be used
               multiple times, to exclude more than one thing. The item is
               typically part of a filename, and any file containing the
               specified text will be excluded.

           -A, --all
               Makes files or other items that are specified on the command
               line take effect in ALL packages acted on, not just the first.

## [](#BUILD_SYSTEM_OPTIONS)BUILD SYSTEM OPTIONS

           The following command line options are supported by all of the
           dh_auto_* debhelper programs. These programs support a variety of
           build systems, and normally heuristically determine which to use,
           and how to use them.  You can use these command line options to
           override the default behavior.  Typically these are passed to
           dh(1), which then passes them to all the dh_auto_* programs.

           -Sbuildsystem, --buildsystem=buildsystem
               Force use of the specified buildsystem, instead of trying to
               auto-select one which might be applicable for the package.

               Pass none as buildsystem to disable auto-selection.

           -Ddirectory, --sourcedir=directory, --sourcedirectory=directory
               Assume that the original package source tree is at the
               specified directory rather than the top level directory of the
               Debian source package tree.

               Warning: The --sourcedir variant matches a similar named
               option in dh_install and dh_missing (etc.) for historical
               reasons.  While they have a similar name, they have very
               distinct purposes and in some cases it can cause errors when
               this variant is passed to dh (when then passes it on to all
               tools).

           -B[directory], --builddir[=directory],
           --builddirectory[=directory]
               Enable out of source building and use the specified directory
               as the build directory. If directory parameter is omitted, a
               default build directory will be chosen.

               If this option is not specified, building will be done in
               source by default unless the build system requires or prefers
               out of source tree building.  In such a case, the default
               build directory will be used even if --builddirectory is not
               specified.

               If the build system prefers out of source tree building but
               still allows in source building, the latter can be re-enabled
               by passing a build directory path that is the same as the
               source directory path.

           --parallel, --no-parallel
               Control whether parallel builds should be used if underlying
               build system supports them.  The number of parallel jobs is
               controlled by the DEB_BUILD_OPTIONS environment variable
               ("Debian Policy, section 4.9.1") at build time. It might also
               be subject to a build system specific limit.

               If neither option is specified, debhelper currently defaults
               to --parallel in compat 10 (or later) and --no-parallel
               otherwise.

               As an optimization, dh will try to avoid passing these options
               to subprocesses, if they are unnecessary and the only options
               passed.  Notably this happens when DEB_BUILD_OPTIONS does not
               have a parallel parameter (or its value is 1).

           --max-parallel=maximum
               This option implies --parallel and allows further limiting the
               number of jobs that can be used in a parallel build. If the
               package build is known to only work with certain levels of
               concurrency, you can set this to the maximum level that is
               known to work, or that you wish to support.

               Notably, setting the maximum to 1 is effectively the same as
               using --no-parallel.

           --reload-all-buildenv-variables
               By default, dh(1) will compute several environment variables
               (e.g. by using dpkg-buildflags(1)) and cache them to avoid
               having all dh_auto_* tool recompute them.

               When passing this option, the concrete dh_auto_* tool will
               ignore the cache from dh(1) and retrigger a rebuild of these
               variables.  This is useful in the very rare case where the
               package need to do multiple builds but with different ...FLAGS
               options.  A concrete example would be needing to change the -O
               parameter in CFLAGS in the second build:

                   export DEB_CFLAGS_MAINT_APPEND=-O3

                   %:
                       dh $@

                   override_dh_auto_configure:
                       dh_auto_configure -Bbuild-deb ...
                       DEB_CFLAGS_MAINT_APPEND=-Os dh_auto_configure \
                          --reload-all-buildenv-variables -Bbuild-udeb ...

               Without --reload-all-buildenv-variables in the second call to
               dh_auto_configure(1), the change in DEB_CFLAGS_MAINT_APPEND
               would be ignored as dh_auto_configure(1) would use the cached
               value of CFLAGS set by dh(1).

               This option is only available with debhelper (>= 12.7~) when
               the package uses compatibility level 9 or later.

           --list, -l
               List all build systems supported by debhelper on this system.
               The list includes both default and third party build systems
               (marked as such). Also shows which build system would be
               automatically selected, or which one is manually specified
               with the --buildsystem option.

## [](#COMPATIBILITY_LEVELS)COMPATIBILITY LEVELS

           From time to time, major non-backwards-compatible changes need to
           be made to debhelper, to keep it clean and well-designed as needs
           change and its author gains more experience. To prevent such major
           changes from breaking existing packages, the concept of debhelper
           compatibility levels was introduced. You must tell debhelper which
           compatibility level it should use, and it modifies its behavior in
           various ways.

           In current debhelper, you can specify the compatibility level in
           debian/control by adding a Build-Depends on the debhelper-compat
           package.  For example, to use v14 mode, ensure debian/control has:

             Build-Depends: debhelper-compat (= 14)

           This also serves as an appropriate versioned build dependency on a
           sufficient version of the debhelper package, so you do not need to
           specify a separate versioned build dependency on the debhelper
           package unless you need a specific point release of debhelper
           (such as for the introduction of a new feature or bugfix within a
           compatibility level).

           Note that debhelper does not provide debhelper-compat for
           experimental or beta compatibility levels; packages experimenting
           with those compatibility levels should put the compat level in the
           X-DH-Compat field of the Source stanza of the debian/control file
           (or, if only for selected commands, the DH_COMPAT environment
           variable).

           Historically, debhelper required specifying the compatibility
           level in the file debian/compat, and debhelper up to version 14
           supports this for backward compatibility. To use this method, the
           debian/compat file should contain the compatibility level as a
           single number, and no other content. If you specify the
           compatibility level by this method, your package will also need a
           versioned build dependency on a version of the debhelper package
           equal to (or greater than) the compatibility level your package
           uses. So, if you specify compatibility level 14 in debian/compat,
           ensure debian/control has:

             Build-Depends: debhelper (>= 14~)

           Note that you must use exactly one method for specifying the
           default debhelper compat level of the package. Whenever possible,
           the debhelper-compat build-dependency is recommended.

           If needed be, the DH_COMPAT environment variable can be used to
           override the compat level for a given command.  The feature is
           mostly useful for either temporarily upgrading a few commands to a
           new compat level or keeping a few commands on a lower compat
           level.  The feature is best used sparingly as it effectively
           introduces special-cases into the debian/rules file that may be
           surprising to maintainers or reviewers (or, in the long term, to
           yourself). Setting a global DH_COMPAT environment variable is not
           recommended.

           Unless otherwise indicated, all debhelper documentation assumes
           that you are using the most recent compatibility level, and in
           most cases does not indicate if the behavior is different in an
           earlier compatibility level, so if you are not using the most
           recent compatibility level, you're advised to read below for notes
           about what is different in earlier compatibility levels.

       Supported compatibility levels
           The list of supported compatibility levels and the related upgrade
           check list has moved to debhelper-compat-upgrade-checklist(7).

## [](#NOTES)NOTES

       Multiple binary package support
           If your source package generates more than one binary package,
           debhelper programs will default to acting on all binary packages
           when run. If your source package happens to generate one
           architecture dependent package, and another architecture
           independent package, this is not the correct behavior, because you
           need to generate the architecture dependent packages in the
           binary-arch debian/rules target, and the architecture independent
           packages in the binary-indep debian/rules target.

           To facilitate this, as well as give you more control over which
           packages are acted on by debhelper programs, all debhelper
           programs accept the -a, -i, -p, and -s parameters. These
           parameters are cumulative.  If none are given, debhelper programs
           default to acting on all packages listed in the control file, with
           the exceptions below.

           First, any package whose Architecture field in debian/control does
           not match the DEB_HOST_ARCH architecture will be excluded ("Debian
           Policy, section 5.6.8").

           Also, some additional packages may be excluded based on the
           contents of the DEB_BUILD_PROFILES environment variable and
           Build-Profiles fields in binary package stanzas in debian/control,
           according to the draft policy at
           <https://wiki.debian.org/BuildProfileSpec>.

           Interaction between package selections and Build-Profiles

           Build-Profiles affect which packages are included in the package
           selections mechanisms in debhelper.  Generally, the package
           selections are described from the assumption that all packages are
           enabled.  This section describes how the selections react when a
           package is disabled due to the active Build-Profiles (or lack of
           active Build-Profiles).

           -a/--arch, -i/--indep OR no selection options (a raw "dh_X" call)
               The package disabled by Build-Profiles is silently excluded
               from the selection.

               Note you will receive a warning if all packages related to
               these selections are disabled.  In that case, it generally
               does not make sense to do the build in the first place.

           -N package / --no-package package
               The option is accepted and effectively does nothing.

           -p package / --package package
               The option is accepted, but debhelper will not act on the
               package.

           Note that it does not matter whether a package is enabled or
           disabled by default.

       Automatic generation of Debian install scripts
           Some debhelper commands will automatically generate parts of
           Debian maintainer scripts. If you want these automatically
           generated things included in your existing Debian maintainer
           scripts, then you need to add #DEBHELPER# to your scripts, in the
           place the code should be added.  #DEBHELPER# will be replaced by
           any auto-generated code when you run dh_installdeb.

           If a script does not exist at all and debhelper needs to add
           something to it, then debhelper will create the complete script.

           When inserting the #DEBHELPER# token into a script, consider
           whether any of the hand written code has a compelling reason to
           appear before the #DEBHELPER# token. The #DEBHELPER# token will
           generally contain the code that start (postinst) or stop
           (prerm/preinst) any services the package is providing. Often (but
           not always), it is better to let the code from #DEBHELPER# run
           first. Common exceptions include things like set -e, initializing
           debconf (when needed) and special-cases like generation or
           hand-written management of configuration files. These things
           should generally occur before the #DEBHELPER# token.

           All debhelper commands that automatically generate code in this
           way let it be disabled by the -n parameter (see above).

           Note that the inserted code will be shell code, so you cannot
           directly use it in a Perl script. If you would like to embed it
           into a Perl script, here is one way to do that (note that I made
           sure that $1, $2, etc are set with the set command):

             my $temp="set -e\nset -- @ARGV\n" . << 'EOF';
             #DEBHELPER#
             EOF
             if (system($temp)) {
                my $exit_code = ($? >> 8) & 0xff;
                my $signal = $? & 0x7f;
                if ($exit_code) {
                    die("The debhelper script failed with error code: ${exit_code}");
                } else {
                    die("The debhelper script was killed by signal: ${signal}");
                }
             }

       Automatic generation of miscellaneous dependencies.
           Some debhelper commands may make the generated package need to
           depend on some other packages. For example, if you use
           dh_installdebconf(1), your package will generally need to depend
           on debconf. Or if you use dh_installxfonts(1), your package will
           generally need to depend on a particular version of xutils.
           Keeping track of these miscellaneous dependencies can be annoying
           since they are dependent on how debhelper does things, so
           debhelper offers a way to automate it.

           As of compat 14, debhelper will automatically inject the relevant
           dependencies for you, since the dependency is done via a
           "relationship substvar" (see
           <https://lists.debian.org/debian-devel/2024/02/msg00230.html> and
           <https://lists.debian.org/debian-devel/2024/03/msg00030.html> for
           details).

           In earlier compat levels, you have to manually specify the
           relevant substvars in the relevant fields. Typically,
           ${misc:Depends} for the Depends field and ${misc:Pre-Depends} for
           the Pre-Depends fields.

           The variables listed here are entirely independent of the standard
           ${shlibs:Depends} generated by dh_makeshlibs(1), and the
           ${perl:Depends} generated by dh_perl(1). For compat 13 and earlier
           you will also have to add these to the respective fields when
           relevant.

       Package build directories
           By default, all debhelper programs assume that the temporary
           directory used for assembling the tree of files in a package is
           debian/package.

           Sometimes, you might want to use some other temporary directory.
           This is supported by the -P flag. For example, "dh_installdocs
           -Pdebian/tmp", will use debian/tmp as the temporary directory.
           Note that if you use -P, the debhelper programs can only be acting
           on a single package at a time. So if you have a package that
           builds many binary packages, you will need to also use the -p flag
           to specify which binary package the debhelper program will act on.

       udebs
           Debhelper includes support for udebs. To create a udeb with
           debhelper, add "Package-Type: udeb" to the package's stanza in
           debian/control.  Debhelper will try to create udebs that comply
           with debian-installer policy, by making the generated package
           files end in .udeb, not installing any documentation into a udeb,
           skipping over preinst, postrm, prerm, and config scripts, etc.

## [](#ENVIRONMENT)ENVIRONMENT

           This section describes some of the environment variables that
           influences the behaviour of debhelper or which debhelper interacts
           with.

           It is important to note that these must be actual environment
           variables in order to affect the behaviour of debhelper (not
           simply Makefile variables).  To specify them properly in
           debian/rules, be sure to "export" them. For example, "export
           DH_VERBOSE".

           DH_VERBOSE
               Set to a non-empty value to enable verbose mode.  Please see
               the -v / --verbose option for details.

           DH_QUIET
               Set to a non-empty value to enable quiet mode. Debhelper will
               not output commands calling the upstream build system nor will
               dh print which subcommands are called and depending on the
               upstream build system might make that more quiet, too.  This
               makes it easier to spot important messages but makes the
               output quite useless as buildd log.

               Ignored if DH_VERBOSE is also set or -v / --verbose is passed.

           DH_COMPAT
               Temporarily specifies what compatibility level debhelper
               should run at, overriding the default compat level of the
               source package.

           DH_NO_ACT
               Set to 1 to enable no-act mode.

           DH_OPTIONS
               All debhelper tools will parse command line arguments listed
               in this variable before any command option (as if they had
               been prepended to the command line arguments).  Unfortunately,
               some third-party provided tools may not support this variable
               and will ignore these command line arguments.

               When using dh(1), it can be passed options that will be passed
               on to each debhelper command, which is generally better than
               using DH_OPTIONS.

           DH_ALWAYS_EXCLUDE
               If set, this adds the value the variable is set to to the -X
               options of all commands that support the -X option. Moreover,
               dh_builddeb will rm -rf anything that matches the value in
               your package build tree.

               This can be useful if you are doing a build from a CVS source
               tree, in which case setting DH_ALWAYS_EXCLUDE=CVS will prevent
               any CVS directories from sneaking into the package you build.
               Or, if a package has a source tarball that (unwisely) includes
               CVS directories, you might want to export
               DH_ALWAYS_EXCLUDE=CVS in debian/rules, to make it take effect
               wherever your package is built.

               Multiple things to exclude can be separated with colons, as in
               DH_ALWAYS_EXCLUDE=CVS:.svn

           DH_EXTRA_ADDONS
               If set, this adds the specified dh addons to be run in the
               appropriate places in the sequence of commands. This is
               equivalent to specifying the addon to run with the --with flag
               in the debian/rules file. Any --without calls specifying an
               addon in this environment variable will not be run.

               This is intended to be used by downstreams or specific local
               configurations that require a debhelper addon to be run during
               multiple builds without having to patch a large number of
               rules file. If at all possible, this should be avoided in
               favor of a --with flag in the rules file.

           DH_COLORS, DPKG_COLORS
               These variables can be used to control whether debhelper
               commands should use colors in their textual output.  Can be
               set to "always", "auto" (the default), or "never".

               Note that DPKG_COLOR also affects a number of dpkg related
               tools and debhelper uses it on the assumption that you want
               the same color setting for dpkg and debhelper.  In the
               off-hand chance you want different color setting for
               debhelper, you can use DH_COLORS instead or in addition to
               DPKG_COLORS.

           NO_COLOR
               If no explicit request for color has been given (e.g.
               DH_COLORS and DPKG_COLORS are both unset), the presence of
               this environment variable cause the default color setting to
               be "never".

               The variable is defined according to <https://no-color.org/>.
               In this project, the environment variables (such as DH_COLORS)
               are considered an explicit request for color.

           CFLAGS, CPPFLAGS, CXXFLAGS, OBJCFLAGS, OBJCXXFLAGS, GCJFLAGS,
           FFLAGS, FCFLAGS, LDFLAGS
               By default (in any non-deprecated compat level), debhelper
               will automatically set these flags by using
               dpkg-buildflags(1), when they are unset.  If you need to
               change the default flags, please use the features from
               dpkg-buildflags(1) to do this (e.g.
               DEB_BUILD_MAINT_OPTIONS=hardening=all or
               DEB_CPPFLAGS_MAINT_APPEND=-DCUSTOM_MACRO=true) rather than
               setting the concrete variable directly.

           HOME, XDG_*
               In compat 13 and later, these environment variables are reset
               before invoking the upstream build system via the dh_auto_*
               helpers.  The variables HOME (all dh_auto_* helpers) and
               XDG_RUNTIME_DIR (dh_auto_test only) will be set to a writable
               directory. All remaining variables and XDG_RUNTIME_DIR (except
               for during dh_auto_test) will be cleared.

               The HOME directory will be created as an empty directory but
               it will be reused between calls to dh_auto_*.  Any content
               will persist until explicitly deleted or dh_clean.

           DEB_BUILD_OPTIONS
               Please see "Supported flags in DEB_BUILD_OPTIONS" for this
               environment variable.

               Please note that this variable should not be altered by
               package maintainers inside debian/rules to change the
               behaviour of debhelper.  Instead, where the package maintainer
               need these features, they should look disabling the relevant
               feature directly (e.g. by overriding the concrete tools).

           DEB_BUILD_MAINT_OPTIONS
               This is a dpkg specific environment variable (see e.g.
               dpkg-buildflags(1)).  The debhelper tool suite silently
               ignores it.

               It is documented here because it has a similar name to
               DEB_BUILD_OPTIONS, which make some people mistakenly assume
               that debhelper will also react to this variable.

       Supported flags in DEB_BUILD_OPTIONS
           The debhelper tool suite reacts to the following flags in
           DEB_BUILD_OPTIONS.

           dherroron=obsolete-compat-levels
               This is a debhelper specific value.

               When dherroron is present and set to obsolete-compat-levels,
               then debhelper tools will promote deprecation warnings for
               usage of old soon to be removed compat levels into errors.

               This is useful for automated checking for code relying on
               deprecated compat levels that is scheduled for removal.

               This option is intended for testing purposes; not production
               builds.

           nostrip
               This value will change the content of the debs being built.
               The .deb packages built when this is set is therefore not
               bit-for-bit reproducible with a regular build in the general
               case.

               This value will cause the official debhelper tools will skip
               actions and helpers that either remove, detach or deduplicate
               debugging symbols in ELF binaries.

               This value affects dh_dwz(1) and dh_strip(1).

           nocheck
               This value will cause the official debhelper build systems to
               skip runs of upstream test suites.

               Package maintainers looking to avoid running the upstream
               tests should not rely on this.  Instead, they can add an empty
               override target to skip dh_auto_test.

               This value affects dh_auto_test(1).

           nodoc
               This value will change the content of the debs being built.
               The .deb packages built when this is set is therefore not
               bit-for-bit reproducible with a regular build in the general
               case.

               This value will cause several debhelper tools to skip
               installation of documentation such as manpages or upstream
               provided documentation.  Additionally, the tools will also
               ignore if declared documentation is "missing" on the
               assumption that the documentation has not been built.

               This value effects tools like dh_installdocs(1), which knows
               it is working with documentation.

           notrimdch
               This value will change the content of the debs being built.
               The .deb packages built when this is set is therefore not
               bit-for-bit reproducible with a regular build in the general
               case.

               This value will cause dh_installchangelogs(1) to act as if it
               had been passed the --no-trim option, forcing it to forgo
               removing older entries from changelogs.

           noautodbgsym, noddebs
               The official name is noautodbgsym.  The noddebs variant is
               accepted for historical reasons.

               This value causes debhelper to skip the generation of
               automatically generated debug symbol packages.

               This value affects dh_strip(1).

           parallel=N
               This value enables debhelper to use up to N threads or
               processes (subject to parameters like --no-parallel and
               --max-parallel=M).  Not all debhelper tools work with parallel
               tasks and may silently ignore the request.

               This value affects many debhelper tools.  Most notably
               dh_auto_*, which will attempt to run the underlying upstream
               build system with that number of threads.

           terse
               This value will cause the official debhelper build systems to
               configure upstream builds to be terse (i.e. reduce verbosity
               in their output).  This is subject to the upstream and the
               debhelper build system supporting such features.

               This value affects most dh_auto_* tools directly. For commands
               provided by the debhelper package, it also causes the tools to
               act like the DH_QUIET environment variable was non-empty.

           Unknown flags are silently ignored.

           Note third-party debhelper-like tools or third-party provided
           build systems may or may not react to the above flags.  This tends
           to depend on implementation details of the tool.

## [](#SEE_ALSO)SEE ALSO

           debhelper-compat-upgrade-checklist(7)
               List of supported compat levels and an upgrade checklist for
               each of them.

           /usr/share/doc/debhelper/examples/
               A set of example debian/rules files that use debhelper.

           <http://joeyh.name/code/debhelper/>
               Debhelper web site.

## [](#AUTHOR)AUTHOR

           Joey Hess <joeyh@debian.org>

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

Pages that refer to this page: [dh(1)](../man1/dh.1.html),  [dh_assistant(1)](../man1/dh_assistant.1.html),  [dh_auto_build(1)](../man1/dh_auto_build.1.html),  [dh_auto_clean(1)](../man1/dh_auto_clean.1.html),  [dh_auto_configure(1)](../man1/dh_auto_configure.1.html),  [dh_auto_install(1)](../man1/dh_auto_install.1.html),  [dh_auto_test(1)](../man1/dh_auto_test.1.html),  [dh_builddeb(1)](../man1/dh_builddeb.1.html),  [dh_clean(1)](../man1/dh_clean.1.html),  [dh_compress(1)](../man1/dh_compress.1.html),  [dh_computeautosubstvars(1)](../man1/dh_computeautosubstvars.1.html),  [dh_dwz(1)](../man1/dh_dwz.1.html),  [dh_fixperms(1)](../man1/dh_fixperms.1.html),  [dh_gencontrol(1)](../man1/dh_gencontrol.1.html),  [dh_install(1)](../man1/dh_install.1.html),  [dh_installalternatives(1)](../man1/dh_installalternatives.1.html),  [dh_installcatalogs(1)](../man1/dh_installcatalogs.1.html),  [dh_installchangelogs(1)](../man1/dh_installchangelogs.1.html),  [dh_installcron(1)](../man1/dh_installcron.1.html),  [dh_installdeb(1)](../man1/dh_installdeb.1.html),  [dh_installdebconf(1)](../man1/dh_installdebconf.1.html),  [dh_installdirs(1)](../man1/dh_installdirs.1.html),  [dh_installdocs(1)](../man1/dh_installdocs.1.html),  [dh_installemacsen(1)](../man1/dh_installemacsen.1.html),  [dh_installexamples(1)](../man1/dh_installexamples.1.html),  [dh_installgsettings(1)](../man1/dh_installgsettings.1.html),  [dh_installifupdown(1)](../man1/dh_installifupdown.1.html),  [dh_installinfo(1)](../man1/dh_installinfo.1.html),  [dh_installinit(1)](../man1/dh_installinit.1.html),  [dh_installinitramfs(1)](../man1/dh_installinitramfs.1.html),  [dh_installlogcheck(1)](../man1/dh_installlogcheck.1.html),  [dh_installlogrotate(1)](../man1/dh_installlogrotate.1.html),  [dh_installman(1)](../man1/dh_installman.1.html),  [dh_installmanpages(1)](../man1/dh_installmanpages.1.html),  [dh_installmenu(1)](../man1/dh_installmenu.1.html),  [dh_installmime(1)](../man1/dh_installmime.1.html),  [dh_installmodules(1)](../man1/dh_installmodules.1.html),  [dh_installpam(1)](../man1/dh_installpam.1.html),  [dh_installppp(1)](../man1/dh_installppp.1.html),  [dh_installsystemd(1)](../man1/dh_installsystemd.1.html),  [dh_installsystemduser(1)](../man1/dh_installsystemduser.1.html),  [dh_installsysusers(1)](../man1/dh_installsysusers.1.html),  [dh_installtmpfiles(1)](../man1/dh_installtmpfiles.1.html),  [dh_installudev(1)](../man1/dh_installudev.1.html),  [dh_installwm(1)](../man1/dh_installwm.1.html),  [dh_installxfonts(1)](../man1/dh_installxfonts.1.html),  [dh_link(1)](../man1/dh_link.1.html),  [dh_listpackages(1)](../man1/dh_listpackages.1.html),  [dh_makeshlibs(1)](../man1/dh_makeshlibs.1.html),  [dh_md5sums(1)](../man1/dh_md5sums.1.html),  [dh_missing(1)](../man1/dh_missing.1.html),  [dh_movefiles(1)](../man1/dh_movefiles.1.html),  [dh_movetousr(1)](../man1/dh_movetousr.1.html),  [dh_perl(1)](../man1/dh_perl.1.html),  [dh_prep(1)](../man1/dh_prep.1.html),  [dh_shlibdeps(1)](../man1/dh_shlibdeps.1.html),  [dh_strip(1)](../man1/dh_strip.1.html),  [dh_systemd_enable(1)](../man1/dh_systemd_enable.1.html),  [dh_systemd_start(1)](../man1/dh_systemd_start.1.html),  [dh_testdir(1)](../man1/dh_testdir.1.html),  [dh_testroot(1)](../man1/dh_testroot.1.html),  [dh_ucf(1)](../man1/dh_ucf.1.html),  [dh_update_autotools_config(1)](../man1/dh_update_autotools_config.1.html),  [dh_usrlocal(1)](../man1/dh_usrlocal.1.html),  [debhelper-compat-upgrade-checklist(7)](../man7/debhelper-compat-upgrade-checklist.7.html),  [debhelper-obsolete-compat(7)](../man7/debhelper-obsolete-compat.7.html)

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
