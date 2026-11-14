---
{"title": "dh_assistant(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh_assistant.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh_assistant(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [COMMAND TAGS](#COMMAND_TAGS) \| [JSON OUTPUT](#JSON_OUTPUT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                  |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH_ASSISTANT(1)                 Debhelper                 DH_ASSISTANT(1)

## [](#NAME)NAME

           dh_assistant - tool for supporting debhelper tools and provide
           introspection

## [](#SYNOPSIS)SYNOPSIS

           dh_assistant command [additional options]

## [](#DESCRIPTION)DESCRIPTION

           dh_assistant is a debhelper program that provides introspection
           into the debhelper stack to assist third-party tools (e.g.
           linters) or third-party debhelper implementations not using the
           debhelper script API (e.g., because they are not written in Perl).

## [](#COMMANDS)COMMANDS

           The dh_assistant supports the following commands:

       active-compat-level (AJSON)
           Synopsis: dh_assistant active-compat-level

           Outputs information about which compat level the package is using.

           For packages without valid debhelper compatibility information
           (whether missing, ambiguous, not supported or simply invalid),
           this command operates on a "best effort" basis and may abort when
           error instead of providing data.

           The returned JSON dictionary contains the following key-value
           pairs:

           active-compat-level
               The compat level that debhelper will be using.  This is the
               same as DH_COMPAT when present or else declared-compat-level.
               This can be null when no compat level can be detected.

           declared-compat-level
               The compat level that the package declared as its default
               compat level.  This can be null if the package does not
               declare any compat level at all.

           declared-compat-level-source
               Defines how the compat level was declared.  This is null (for
               the same reason as declared-compat-level) or one of:

               debian/compat
                   The compatibility level was declared in the single line
                   debian/compat file.

               X-DH-Compat: <C>
                   The compatibility was declared in the debian/control via a
                   the X-DH-Compat field. In the output, the C is replaced by
                   the actual compatibility level.  A full example value
                   would be:

                      X-DH-Compat: 15

               Build-Depends: debhelper-compat (= <C>)
                   The compatibility was declared in the debian/control via a
                   build dependency on the debhelper-compat (= <C>) package
                   in the Build-Depends field.  In the output, the C is
                   replaced by the actual compatibility level.  A full
                   example value would be:

                      Build-Depends: debhelper-compat (= 15)

       supported-compat-levels (AJSON, CRFA)
           Synopsis: dh_assistant supported-compat-levels

           Outputs information about which compat levels, this build of
           debhelper knows about.

           This command accepts no options or arguments.

       which-build-system (AJSON)
           Synopsis: dh_assistant which-build-system [build step]
           [build system options]

           Output information about which build system would be used for a
           particular build step.  The build step must be one of configure,
           build, test, install or clean and must be the first argument after
           which-build-system when provided.  If omitted, it defaults to
           configure as it is the most reliable step to use auto-detection on
           in a clean source directory.  Note that build steps do not always
           agree when using auto-detection - particularly if the configure
           step has not been run.

           Additionally, the clean step can also provide "surprising" results
           for builds that rely on a separate build directory.  In such
           cases, debhelper will return the first build system that uses a
           separate build directory rather than the one build system that
           configure would detect.  This is generally a cosmetic issue as
           both build systems are all basically a glorified rm -fr builddir
           and more precise detection is functionally irrelevant as far as
           debhelper is concerned.

           The option accepts all debhelper build system arguments - i.e.,
           options you can pass to all of the dh_auto_* commands plus (for
           the install step) the --destdir option.  These options affect the
           output and auto-detection in various ways.  Passing -S or
           --buildsystem overrides the auto-detection (as it does for
           dh_auto_*) but it still provides introspection into the chosen
           build system.

           Things that are useful to know about the output:

           •   The key build-system is the build system that would be used by
               debhelper for the given step (with the given options,
               debhelper compat level, environment variables and the given
               working directory).  When -S and --buildsystem are omitted,
               this is the result of debhelper's auto-detection logic.

               The value is valid as a parameter for the --buildsystem
               option.

               The special value "none" is used to denote that no build
               system would be used (that is, a JSON string).  This value is
               not present in --list parameter for the dh_auto_* commands,
               but since debhelper/12.9 the value is accepted for the
               --buildsystem option.

               Note that auto-detection is subject to limitations in regards
               to third-party build systems.  While debhelper does support
               auto-detecting some third-party build systems, they must be
               installed for the detection to work.  If they are not
               installed, the detection logic silently skips that build
               system (often resulting in build-system being "none" in the
               output).

           •   The build-directory and buildpath values serve different but
               related purposes.  The build-directory generally mirrors the
               --builddirectory option where as buildpath is the output
               directory that debhelper will use.  Therefore the former will
               often be null when --builddirectory has not been passed while
               the latter will generally not be null (except when
               build-system is none).

           •   The dest-directory (--destdir) is undefined for all build
               steps except the install build step (will be output as null or
               absent).  For the same reason, --destdir should only be passed
               for install build step.

               Note that if not specified, this value is currently null by
               default.

           •   The parallel value is subject to DEB_BUILD_OPTIONS.  Notably,
               if that does not include the parallel keyword, then parallel
               field in the output will always be 1.

           •   Most fields in the output can be null.  Particular if there is
               no build system is detected (or when --buildsystem=none).
               Additionally, many of the fields can be null even if there is
               a build system if the build system does not use/set/define
               that variable.

       parse-dh-cli-args (AJSON, BLD)
           Synopsis:  dh_assistant parse-dh-cli-args dh_assistant-options --
           command-line-options

           Parses command-line-options like a dh_* command would and output a
           JSON document with the result.

           This subcommand is aimed at supporting third-party commands in
           implementing the debhelper command-line parsing logic. The rules
           look deceptively simple but turns out to be very complex, which
           means that tools not written using the Debian::Debhelper::Dh_Lib
           module will be at a massive disadvantage.  As a consequence,
           consumers get a mixed result since some times behave differently
           to the same options than others.

           This command reacts to option parsing like any built debhelper
           command and therefore accounts for DH_OPTIONS and other such
           environment variables. However, since dh_assistant has to parse
           the options without knowing all arguments, it might get command
           specific options wrong if the value looks like option. As an
           example, if dh_assistant sees --foo -a, it assumes -a is the
           debhelper -a and leaves --foo as unparsed. If --foo always takes a
           parameter in the caller, then this is the wrong behavior. This
           ambiguity can be avoided if --foo=-a is passed instead. This
           problem can also occur due to "bundling" such as -fa (which
           debhelper reads as the two independent options -f -a. This is for
           the caller to avoid.

           If the command returns successfully, the output will be JSON
           describing the options (see description below for the details).
           Otherwise, there will be a human readable error on stderr for what
           went wrong. Note that stderr can also be used to emit warnings on
           a successful run.

           The command-line-options should be the command line options the
           caller wish to have parsed on their behalf.

           Options specific for dh_assistant

           The command accepts the following arguments in the place of
           dh_assistant-options:

           --on-behalf-of-cmd=COMMAND (mandatory)
               The name of the command calling.

           --masquerade, --no-masquerade (optional)
               Whether dh_assistant should pretend to be the caller if it
               outputs any warnings or errors.

               By default, it will use its own name but mention the calling
               command. When --masquerade is passed, only the calling
               commands name will be listed in the log file. The difference
               being whether the user sees:

                 dh_assistant (for dh_command): ...

               vs.

                 dh_command: ...

               Though, this option is only relevant if the stderr of the
               dh_assistant process is not redirected away.

           --inhibit-log, --no-inhibit-log (optional)
               Whether dh_assistant should write to the debhelper log that
               the command has acted on the packages (when that is relevant).
               Any package name listed in active-packages of the output will
               be marked as acted on in the log when the log is used and
               --inhibit-log is used (which is the default).

               This is necessary for --remaining-packages to work correctly
               in hook targets.

               If --no-inhibit-log is passed, the caller must update the log
               themselves on successful completion of the command.

           --noop-warnings, --no-noop-warnings (optional)
               It is possible for a command to end up in a situation where
               the command line options plus the current build implies there
               are no packages to be acted on. This results in the
               active-packages key of the output being an empty list.

               Generally, the correct answer here is to output a warning and
               exit successfully despite having done nothing. By default
               (--noop-warnings), dh_assistant emits these warnings on behalf
               of the caller. The --no-noop-warnings can be used if the
               warning is undesirable for some reason.

           JSON output format

           The output of this command is a JSON document of

             {
               "active-packages": ["debhelper"],
               "debhelper-settings": {
                 "exclude": [],
                 "no-act": false,
                 "no-scripts": false,
                 "quiet": false,
                 "requested-staging-dir": null,
                 "verbose": false
               },
               "options": {
                 "--all": false,
                 "--name": null,
                 "-d": null,
                 "-v": null,
                 "args": [],
                 "try-args": []
               },
               "packages": {
                 "debhelper": {
                    "binary-arch": "all",
                    "declared-arch": "all",
                    "package-type": "deb"
                 }
               }
             }

           The keys have the following definition:

           active-packages
               List of packages to act on.

               This list can be empty if the user requested packages that
               cannot be built. This can occur with -a when all packages are
               Architecture: all as an example.

               The value is always included and never null.

           debhelper-settings
               This is an object of common and well defined debhelper options
               that might be of interest. Not all of these have a 1:1 with a
               command line option (quiet is a consequence of no -v combined
               with DEB_BUILD_OPTIONS=terse), but they are still provided
               here for simplicity.

               The object is always included and never null.

               The following key-value pairs are defined in this object:

               verbose, quiet
                   The verbose and quiet values  define how verbose the
                   command should be. They are never both true at the same
                   time as debhelper prefers -v (verbose) over terse (quiet).
                   However, they can both be false at the same time and this
                   is the default state.

                   The verbose option is triggered by options like -v,
                   --verbose or the DH_VERBOSE environment variable. The
                   quiet option is triggered things like DEB_BUILD_OPTIONS
                   containing terse.

                   The values are always set, boolean and never null.

               no-act
                   When true, the user passed the --no-act option. The
                   command is expected to write what it would do but not
                   actually do it. The accuracy is on a best-effort basis,
                   since actions can have side-effects that affect later
                   actions and those can be difficult to emulate.

                   The value is always set, boolean and never null.

               no-scripts
                   These options correspond to the --no-scripts option.

                   They typically control whether the command should generate
                   maintscripts. When true, the command should skip
                   generation of such script snippets.

                   Some command also use this to control whether triggers are
                   generated for historical reasons.

                   The value is always set, boolean and never null.

               exclude
                   This is a list of all the requested exclusions. Typically
                   from --exclude options.  However, it also includes values
                   from other sources such as ENV variables.

                   It is up to the command to define how exclusions affect
                   them if at all or even how they match. Common examples
                   include substring matching or regexes on filenames.

                   The value is always set, a list and never null, but the
                   list can be empty.

               requested-staging-dir
                   This is a nullable string matching the -P option. If null
                   (the default), then the default per package staging
                   directory should be used (debian/PACKAGE).

                   It only makes sense when there is at most one active
                   package. Note it can appear with no active packages if the
                   command is called unconditionally with -p PKG and the
                   provided package should not be built for some reason.

                   Note: The directory (when provided) can be either relative
                   or absolute based on how the value for the option was
                   defined. Additionally, the directory is not required to
                   exist as tools are expected to create directories as
                   necessary.

           options
               This is an object containing information about command options
               used.

               The object is always present and never null.

               The following key-value pairs are defined in this object:

               --all
                   Whether the --all option was passed. It is a boolean
                   option (never null).

                   This is a niche option and many commands ignore it.

               --name
                   If not null, the --name parameter was passed. For commands
                   that support named configuration files, it defines the
                   named segment of the files and typically also part of the
                   basename the file is installed under (if installed).

                   Many commands ignore this option.

               -d, -V
                   These options are defined as common arguments but with no
                   well-defined meaning.  Commands are free to choose their
                   own definition.

                   The -d is a boolean option (never null). The value is true
                   if -d was passed and false otherwise. The -V is an
                   parameter that optionally takes a string. It will be null,
                   if -V is not passed otherwise it will be a string. The
                   empty string means no value was passed to -V.

               args
                   List of arguments that dh_assistant did not understand and
                   assume are arguments for the caller. Their relative order
                   is preserved but debhelper specific options are removed.
                   As an example, if dh_assistant is passed --foo -a -v bar,
                   then args will be the list ["--foo", "bar"].

                   The value is always present, a list and never null. It can
                   be and often is empty.

               try-args
                   List of arguments that were prefixed with -O and that
                   dh_assistant did not understand.

                   The caller should try to parse each of them individually
                   and accept the ones it understands.  Unknown arguments
                   should be ignored silently.

                   When parameters that accept values are passed via -O they
                   must always be passed with their value as a single
                   argument (such as -O--foo=bar). This is a deeply root
                   assumption in debhelper and caller is expected to follow
                   that assumption rather than conditionally parsing an extra
                   argument.

                   The value is always present, a list and never null. It can
                   be and often is empty.

           packages
               This is an object containing information about packages.

               The object is always present and never null.

               Each key is the name of a package defined in debian/control.
               The values are an object. There is always a key for every
               package defined in debian/control even if they are not listed
               in active-packages.

               The following key-value pairs are defined in the per package
               object object:

               declared-arch
                   This is the value of the Architecture field and therefore
                   a string. That string can be interpreted as a space
                   separated list of architectures or architecture wild
                   cards.

                   If the value is equal to all, then the package is an
                   "arch:all" package.

               binary-arch
                   This is the architecture of this binary package if it is
                   built. Unlike declared-arch this is always a single
                   architecture.

                   If the value is equal to all, then the package is an
                   "arch:all" package.

                   One can be forgiving for assuming this value is always
                   either all or the value of DEB_HOST_ARCH. While that holds
                   in 99.9% of the cases, debhelper supports some very
                   special cases where that is not true. Consumers are
                   recommended to use this value rather than doing their own
                   computation here.

               package-type
                   This is the type of package being built (the Package-Type
                   field).

                   Most commonly the value will be deb. However, udeb is
                   another known value.

       detect-hook-targets (EXEC, AJSON)
           Synopsis: dh_assistant detect-hook-targets

           Detects possible override targets and hook targets that dh(1)
           might use (provided that the relevant command is in the sequence).

           **UNSAFE**: This command relies on the output of make. Even it its
           dry-run mode, make may execute commands from debian/rules. Avoid
           using on packages from untrusted sources, where you have not
           reviewed the packaging for backdoors.

           The detection is based on scanning the rules file for any target
           that might look like a hook target and can therefore list targets
           that are in fact not hook targets (or are but will never be
           triggered for other reasons).

           The detection uses a similar logic for scanning the rules file and
           is therefore subject to makefile conditionals (i.e., the truth
           value of makefile conditionals can change whether a hook target is
           visible in the output of this command).  In theory, you would have
           to setup up the environment to look like it would during a build
           for getting the most accurate output.  Though, a lot of packages
           will not have conditional hook targets, so the "out of the box"
           behaviour will work well in most cases.

           The output looks something like this:

               {
                  "commands-not-in-path": [
                     "dh_foo"
                  ],
                  "hook-targets": [
                     {
                        "command": "dh_strip_nondeterminism",
                        "is-empty": true,
                        "package-section-param": null,
                        "filename": "debian/rules",
                        "target-name": "override_dh_strip_nondeterminism"
                     },
                     {
                        "command": "dh_foo",
                        "is-empty": false,
                        "package-section-param": "-a",
                        "filename": "debian/rules",
                        "target-name": "override_dh_foo-arch"
                     }
                  ]
               }

           In more details:

           commands-not-in-path
               This attribute lists all the commands related to hook targets,
               which dh_assistant could not find in PATH.  These are usually
               caused by either the command not being installed on the system
               where dh_assistant is run or by the command not existing at
               all.

               If you are using this command to verify an hook target is
               present, please double check that the command is spelled
               correctly.

           hook-targets
               List over hook targets found along with additional information
               about them.

               command
                   Attribute that lists which command this hook target is
                   related too.

               target-name
                   The actual target name detected in the debian/rules file.

               is-empty
                   A boolean that determines whether dh(1) will optimize the
                   hook out at runtime (see "Completely empty targets" in
                   dh(1)). Note that empty override targets will still cause
                   dh(1)  to skip the original command.

               package-section-param
                   This attribute defines what package selection parameter
                   should be passed to dh_* commands used in the hook target.
                   It can either be -a, -i or (if no parameter should be
                   used) "null".

               filename
                   This attribute reports which file the target was found it.
                   In most cases, this will always be "debian/rules" though
                   in case of include files, the target could appear in an
                   include file.  Note this attribute is not super reliable
                   as make(1) only reports it for targets with a "recipe"
                   (targets with commands inside them). When make does not
                   provide the filename, dh_assistant blindly assumes the
                   filename is "debian/rules" (as overrides via includes is
                   not a commonly used feature).

                   Note this accuracy of this attribute is limited about what
                   data dh_assistant can read out from the following command:

                       LC_ALL=C make -Rrnpsf debian/rules debhelper-fail-me 2>/dev/null

           This command accepts no options or arguments.

       detect-unknown-hook-targets (EXEC, AJSON, LINT)
           Synopsis: dh_assistant detect-unknown-hook-targets
           [--output-format=json] [command-options]

           Detects unknown and possibly misspelled override targets and hook
           targets in debian/rules that will most likely not be used by
           dh(1).

           **UNSAFE**: This command relies on the output of make. Even it its
           dry-run mode, make may execute commands from debian/rules. Avoid
           using on packages from untrusted sources, where you have not
           reviewed the packaging for backdoors.

           This command differs from detect-hook-targets subtly in the scope.
           The detect-hook-targets will list all targets that looks like hook
           targets whether they are applicable or not. This command show all
           hook targets, for which a command cannot be found in any sequence.
           Accordingly, this command is better for linting purposes whereas
           detect-hook-targets is better if you want to know which hook
           targets are present. All the limitations listed in
           detect-hook-targets about scanning the rules file apply equally to
           this command.

           This command will attempt will attempt to load any sequence add-on
           listed via build-dependencies and therefore these must be
           installed. Additional modules can be passed via --with like with
           dh(1) as needed.

           This command will also need one of the following perl modules to
           be available: Text::Levenshtein, Text::LevenshteinXS,
           Text::Levenshtein::XS. The first one can be installed via apt
           install libtext-levenshtein-perl.

           The text output is intended for human consumption and should be
           self-explanatory.  Since it is not stable, it will not be
           documented. The JSON output looks something like this:

               {
                  "unknown-hook-targets": [
                     {
                        "target-name": "execute_before_dh_instlal",
                        "filename": "debian/rules",
                        "candidates": [
                           "execute_before_dh_install"
                        ]
                     }
                  ],
                 "hook-targets-for-disabled-commands": [
                     {
                        "filename": "debian/rules",
                        "target-name": "override_dh_builddeb",
                        "removed-by": "zz-debputy"
                     }
                  ],

               }

           In more details:

           unknown-hook-targets
               List of all the unknown hook targets found along with
               additional information about them.

               target-name
                   The actual target name detected in the file (usually
                   debian/rules).

               filename
                   This attribute reports which file the target was found it.
                   In most cases, this will always be "debian/rules" though
                   in case of include files, the target could appear in an
                   include file.  Note this attribute is not super reliable
                   as make(1) only reports it for targets with a "recipe"
                   (targets with commands inside them). When make does not
                   provide the filename, dh_assistant blindly assumes the
                   filename is "debian/rules" (as overrides via includes is
                   not a commonly used feature).

                   Note this accuracy of this attribute is limited about what
                   data dh_assistant can read out from the following command:

                       LC_ALL=C make -Rrnpsf debian/rules debhelper-fail-me 2>/dev/null

               candidates
                   When not null and not empty, each element in this list are
                   names for likely candidates for the "correct" name of this
                   target.

           hook-targets-for-disabled-commands
               List of known hook targets found related to disabled commands
               along with additional information about them.

               target-name
                   The actual target name detected in the file (usually
                   debian/rules).

               filename
                   This attribute reports which file the target was found it.
                   In most cases, this will always be "debian/rules" though
                   in case of include files, the target could appear in an
                   include file.  Note this attribute is not super reliable
                   as make(1) only reports it for targets with a "recipe"
                   (targets with commands inside them). When make does not
                   provide the filename, dh_assistant blindly assumes the
                   filename is "debian/rules" (as overrides via includes is
                   not a commonly used feature).

                   Note this accuracy of this attribute is limited about what
                   data dh_assistant can read out from the following command:

                       LC_ALL=C make -Rrnpsf debian/rules debhelper-fail-me 2>/dev/null

               removed-by
                   If present, this denotes the dh add-on that removed the
                   command from the sequence (thereby disabling this command
                   for that package).

                   Note this field is not present in all cases. As an
                   example, as obsolete commands (such as dh_gconf) are not
                   part of any sequence by the time they are marked as
                   obsolete.

                   If you (as a consumer) need to know whether a command is
                   obsolete or the particular reason why a command was
                   disabled, please file a feature request to get that data.
                   The absence of removed-by is not guaranteed to imply the
                   command is obsolete.

           issues
               If present, then it is a list of one or more reasons why this
               output is definitely incomplete. Each element in the list is
               an object with the following keys:

               issue
                   A key defining the issue. Currently, it is always
                   load-addon, which signals that dh_assistant could not load
                   the add-on listed in the addon key.

                   Parsers should assume new issue types may appear in the
                   future.

               addon
                   If present, it defines the name of a dh sequence add-on
                   that is related to the failure.

           This command accepts the following options:

           --output-format=FORMAT
               Request a certain type of output format. Valid values are text
               or json.

               The text format is intended for human consumption and may
               change between versions without any regard for machine
               consumption. If you want to use this command for machine
               consumption, please use the JSON format.

           --no-linter-exit-code, --linter-exit-code
               These options control whether the command should exit with the
               linter exit code (2) or not (0) when an unknown target is
               found. By default, it uses the linter exit code when an
               unknown target is found.

           --with addon, --without addon
               These options behave the same as the dh(1) options with the
               same name.

       list-commands (RJSON)
           Synopsis: dh_assistant list-commands [--output-format=json]
           [command-options]

           Load all dh sequence add-ons and extract a full list of all
           commands that will be invoked across all sequences. The command
           makes no attempt to filter out commands that will not be run due
           to override targets or due to certain sequences not being run (by
           dh or at all).

           As the command will attempt to load all plugins, they must be
           installed.

           The text output is intended for human consumption and should be
           self-explanatory.  Since it is not stable, it will not be
           documented. The JSON output looks something like this:

               {
                  "commands": [
                     {
                        "command": "dh_auto_build"
                     },
                     {
                        "command": "dh_auto_clean"
                     },
                     [... more commands listed here... ]
                  ],
                  "removed-commands": [
                      {
                        "command": "dh_gconf"
                     },
                  ]
                  "issues": [
                       {
                           "issue": "load-addon",
                           "addon": "foo"
                       }
                  ]
               }

           commands
               The top level key containing the list of all commands. Each
               element in the list are an object and can have the following
               keys:

               command
                   The name of the command.

                   While most commands are resolved via PATH, a sequence
                   add-on could register a command via a full path (by
                   passing the path search). If so, the command provided in
                   this output will also use the full path.

           disabled-commands
               The top level key containing the list of all known commands
               that have been disabled. Each element in the list are an
               object and can have the following keys:

               command
                   The name of the command.

                   While most commands are resolved via PATH, a sequence
                   add-on could register a command via a full path (by
                   passing the path search). If so, the command provided in
                   this output will also use the full path.

               removed-by
                   If present, this denotes the dh add-on that removed the
                   command from the sequence (thereby disabling this command
                   for that package).

                   Note this field is not present in all cases. As an
                   example, as obsolete commands (such as dh_gconf) are not
                   part of any sequence by the time they are marked as
                   obsolete.

                   If you (as a consumer) need to know whether a command is
                   obsolete or the particular reason why a command was
                   disabled, please file a feature request to get that data.
                   The absence of removed-by is not guaranteed to imply the
                   command is obsolete.

           issues
               If present, then it is a list of one or more reasons why this
               output is definitely incomplete. Each element in the list is
               an object with the following keys:

               issue
                   A key defining the issue. Currently, it is always
                   load-addon, which signals that dh_assistant could not load
                   the add-on listed in the addon key.

                   Parsers should assume new issue types may appear in the
                   future.

               addon
                   If present, it defines the name of a dh sequence add-on
                   that is related to the failure.

           This command accepts the following options:

           --output-format=FORMAT
               Request a certain type of output format. Valid values are text
               or json.

               The text format is intended for human consumption and may
               change between versions without any regard for machine
               consumption. If you want to use this command for machine
               consumption, please use the JSON format.

           --with addon, --without addon
               These options behave the same as the dh(1) options with the
               same name.

       list-guessed-dh-config-files (AJSON)
           Synopsis: dh_assistant list-guessed-dh-config-files
           [command-options]

           Load all dh sequence add-ons declaratively depended on, determine
           the full list of commands could be relevant for this source
           package and for each command used, then attempt to guess which
           "config files" these commands are interested in.

           The command will include config files for commands that are not
           active with current add-ons, since the commands might be run
           manually from hook targets.

           Note this command only guesses "per command config files".
           Standard global config files such as debian/control, debian/rules,
           and debian/compat are not included in this output.

           As the command name implies, the resulting output is not a full
           list (and will never be).  The dh_assistant tool have to derive
           this from optional metadata that commands can choose to provide
           and dh_assistant has no means to validate that this metadata is up
           to date.

           As the command will attempt to load all plugins referenced by the
           package, they must be installed.

           The text output is intended for human consumption and should be
           self-explanatory.  Since it is not stable, it will not be
           documented. The JSON output looks something like this:

               {
                  "config-files": [
                     {
                        "commands": [
                           {
                              "command": "dh_autoreconf_clean"
                              "is-active": true
                           }
                        ],
                        "file-type": "pkgfile",
                        "pkgfile": "autoreconf.before"
                     },
                     {
                        "commands": [
                           {
                              "command": "dh_installgsettings"
                              "is-active": true
                           }
                        ],
                        "file-type": "pkgfile",
                        "pkgfile": "gsettings-override"
                     },
                     # [ ... more entries here ...]
                  ],
                  "issues": [
                      {
                           "issue": "load-addon",
                           "addon": "foo"
                      }
                  ]
               }

           config-files
               The top level key containing the list of all config-files.
               Each element in the list are an object and can have the
               following keys:

               file-type
                   The type of config file detected. At the time of writing,
                   this will either be pkgfile or path. However, other values
                   may appear in the future.

                   When it is pkgfile, then the config file is a debhelper
                   pkgfile (named after the pkgfile sub in
                   Debian::Debhelper::Dh_Lib that locates the file). The
                   value denoted by the pkgfile key will be the stem of the
                   pkgfile (the install in debian/package. install).

               pkgfile
                   When file-type is pkgfile, this key defines the name stem
                   of the pkgfile. An example, this will be install for
                   dh_install(1)'s config file and docs for
                   dh_installdocs(1)'s config file.

                   When file-type is not pkgfile, then this key will be
                   absent.

                   Typically names for these files are:

                        debian/PKGFILE
                        debian/PACKAGE.PKGFILE

                   However, there are more variants caused by --name plus
                   architecture specific suffixes.

               path
                   When file-type is path, this key defines the static path
                   of the configuration. An example, this will be
                   debian/clean for dh_clean(1)'s config file and
                   debian/not-installed for dh_missing(1).

                   When file-type is not path, then this key will be absent.

               internal
                   This key may exist and any value for it is not
                   standardized. Use at own peril.

                   It used for document certain specific implementation
                   details such as bug compatibility and may change as the
                   situation changes.

               commands
                   This key will be a list with each element in it being an
                   object with the following keys:

                   command
                       Name of the command that is interested in this config
                       file. Multiple commands can be interested in the same
                       config file. An example of this would be
                       dh_installinit, dh_installsystemd and
                       dh_installtmpfiles, which all reacts to (the now)
                       deprecated tmpfile pkgfile. In the particular case,
                       only one command reacts to the file for a given compat
                       level (but that information is not available to
                       dh_assistant and therefore is not available in this
                       output either).

                   is-active
                       A boolean that determines whether the command is
                       active with the loaded sequences. When false, the
                       command is known to debhelper, but it is not run
                       automatically via dh. The command might be explicitly
                       removed by a sequence, marked as obsolete or possibly
                       known to debhelper a command that would activate in a
                       different command level (than the one currently
                       active).

                       Note that commands that are not "active" can often
                       still be invoked manually from debian/rules via hook
                       targets. Therefore, this reflects whether dh would
                       call the command directly or provide its standard hook
                       targets for the command.

                   removed-by
                       If present, this denotes the dh add-on that removed
                       the command from the sequence (thereby disabling this
                       command for that package).

                       Note this field is not present in all cases regardless
                       of the value of is-active. As an example, as obsolete
                       commands (such as dh_gconf) are not part of any
                       sequence by the time they are marked as obsolete.

                       If you (as a consumer) need to know whether a command
                       is obsolete or the particular reason why a command was
                       disabled, please file a feature request to get that
                       data. The absence of removed-by plus is-active being
                       false is not guaranteed to imply the command is
                       obsolete.

           issues
               If present, then it is a list of one or more reasons why this
               output is definitely incomplete. Each element in the list is
               an object with the following keys:

               issue
                   A key defining the issue. Currently, it is always
                   load-addon, which signals that dh_assistant could not load
                   the add-on listed in the addon key.

                   Parsers should assume new issue types may appear in the
                   future.

               addon
                   If present, it defines the name of a dh sequence add-on
                   that is related to the failure.

           This command accepts the following options:

           --with addon, --without addon
               These options behave the same as the dh(1) options with the
               same name.

       log-installed-files (BLD)
           Synopsis: [1mdh_assistant log-installed-files -ppkg
           [--on-behalf-of-cmd=dh_foo] path ...

           Mark one or more paths as installed for a given package.  This is
           useful for telling dh_missing(1) that the paths have been
           installed manually.

           The --on-behalf-of-cmd option can be used by third-party tools to
           have dh_assistant list them as the installer of the provided
           paths.  The convention is to use the basename of the tool itself
           as its name (e.g. dh_install).

           Please keep in mind that:

           •   No glob or substitution expansion is done by dh_assistant on
               the provided paths.  If you want to use globs, have the shell
               perform the expansion first.

           •   Paths must be given as relative to the source root directory
               (e.g., debian/tmp/...)

           •   You can provide a directory.  If you do, the directory and
               anything recursively below it will be considered as installed.
               Note that it is fine to provide the directory even if paths
               inside of it has been excluded as long as the directory is
               fully "covered".

           •   Do not worry about providing the same filename twice in
               different invocations to dh_assistant due to -arch / -indep
               overrides.  While it will be recorded multiple internally,
               dh_missing(1) will deduplicate when it parses the records.

           Note this command only marks paths as installed. It does not
           actually install them - the caller should ensure that the paths
           are in fact handled (or installed).

       restore-file-on-clean (BLD)
           Synopsis: dh_assistant restore-file-on-clean FILE ...

           This command will take a backup of listed files and tell
           dh_clean(1) to restore them when it runs.

           Note that generally you do not need to restore modified files on
           clean. Often you can get away with just removing them if they are
           regenerated anyway (which is the most common case for files being
           modified during builds).  Use this command when something taints a
           file and the build does not cope with the file being removed.

           The file is stored in debian/.debhelper. If you remove this
           directory manually without calling dh_clean(1) then your
           dh_assistant provided backup is gone permanently and the restore
           will never occur. At this point, only a version control system or
           another backup can restore the files.

           The command has the following limitations:

           No thread-safety - concurrency will corrupt the restore
               The command relies on updating an internal index and
               concurrent writes will cause it to be corrupt.

               While most dh_* commands does not use the underlying function,
               any of them could do so. Avoid running another dh_* command
               while dh_assistant processes this command (especially running
               multiple concurrent instances of dh_assistant
               restore-file-on-clean is asking for corruption!).

           Files only, not directories nor symlinks to files
               This command will only restore files; not directories or
               symlinks to files. It will reject any non-files.

               Additionally, if the directory containing the file is removed,
               the restore will fail (as debhelper does not track the
               directory, it cannot restore it reliably). If this happens,
               you can do a mkdir to restore the directory and run
               dh_clean(1) again to get the files back. After that, consider
               what went wrong and whether you are using the correct tool(s).

           Strict file names
               All filenames must be relative to the package root (without
               using the ./ prefix). No hidden files (that is any file
               starting with a period .) and no version control directories
               (such as CVS). The checks are best effort.

               These checks are here to ensure you do not accidentally trash
               important data that would help you undo mistakes.

           Heavy duty
               The command takes a full copy of all files you pass it. This
               is fine for a handful of small files, which is the intended
               use-case. If you find yourself passing 10+ files or very large
               files, you might be applying a sledgehammer where you needed a
               different tool.

       compat-upgrade-checklist (EXEC)
           Synopsis: dh_assistant compat-upgrade-checklist [--target-compat
           N]

           This command generates a compat upgrade checklist for the current
           package.

           The upgrade checklist is intended as an aid for contributors that
           upgrade a package to a newer compat level. Where possible,
           dh_assistant will attempt to detect whether some of the items are
           likely to be irrelevant and mark them as such. The logic will in
           many cases be a heuristic that can have false-positives and
           false-negatives.

           The output is a markdown based checklist template aimed at being
           human-readable (output stability is not a goal). Typically, the
           user will want to direct standard output and then edit the
           checklist as they process to a file a la:

               dh_assistant compat-upgrade-checklist > debian/compat-upgrade-checklist.md
               editor debian/compat-upgrade-checklist.md
               # Iterate through the checklist, tweak the packaging, cross off items from the checklist (rinse and repeat)
               # Finally, remove the checklist.
               rm -f debian/compat-upgrade-checklist.md  # when the migration is complete

           The command will provide a checklist up to latest stable compat
           level or the compat level provided via the --target-compat option.

           This command accepts the following options:

           --target-compat N
               Request the upgrade checklist to stop at the provided compat
               level rather than the highest stable compat level. This option
               can be used to limit the checklist to a given compat level or
               request checklists for experimental compat levels.

               The option cannot be used to generate a checklist for
               downgrading to a previous compat level. Trying to do so will
               result in an error message.

           Note: If you run this command from a git checkout of debhelper,
           the behavior is slight different, since it will not correctly
           track which compat levels are stable (it is a build-time inserted
           property). As such, you will see experimental compat levels in the
           checklists by default, and they will not be marked as such.  If
           you use the git checkout, it falls on you to be extra careful with
           these limitations of the generated checklist.

       supports (CFFA)
           Synopsis: dh_assistant supports COMMAND

           This command is a scripting aid to programmatically determine
           whether dh_assistant knows about a given subcommand. Pass the name
           of a subcommand and this command will exit successfully if the
           subcommand was known and unsuccessfully otherwise.

## [](#COMMAND_TAGS)COMMAND TAGS

           Most commands have one or more of the following "tags" associated
           with them.  Their meaning is defined here.

           EXEC
               This command will or may execute content from the package. Do
               not run on untrusted packages.

               Note: This tag only applies if the command will out of the box
               be unsafe. As an example, commands that parse the output of
               make is inherently unsafe, because it is trivial make to have
               make run code even in --dry-run mode. As a counter example,
               commands that only loads dh add-ons will be considered safe,
               because PERL5LIB is assumed to be curated to only include
               trusted plugins.

           AJSON
               The command always provides JSON output. See "JSON OUTPUT" for
               details.

           RJSON
               The command *can* provide JSON output via
               --output-format=json, but does not do so by default. See "JSON
               OUTPUT" for details when using --output-format=json.

           LINT
               The command is or can be used for linting purposes. This
               command will exit with code 2 when an important issue is
               found. Be careful if the command is also tagged with EXEC.
               When this happens, the command should only be used on trusted
               content (see the EXEC tag for details).

               Note that commands may have options that redefine what is
               considered an "important" issue.

           CRFA
               Mnemonic "Can be Run From Anywhere"

               Most commands must be run inside a source package root
               directory (a directory containing debian/control) because
               debhelper will need the package metadata to lookup the
               information.  Any command with this tag are exempt from this
               requirement and is expected to work regardless of where they
               are run.

           BLD The command is intended to be used as a part of a package
               build. It may leave artifacts behind that will need a
               dh_clean(1) invocation to remove.

## [](#JSON_OUTPUT)JSON OUTPUT

           Most commands uses JSON format as output.  Consumers need to be
           aware that:

           •   Additional keys may be added at any time.  For backwards
               compatibility, the absence of a key should in general be
               interpreted as null unless another default is documented or
               would be "obvious" for that case.

           •   Many keys can be null/undefined in special cases.  As an
               example, some information may be unavailable when this command
               is run directly from the debhelper source (git repository).

           The output will be prettified when stdout is detected as a
           terminal.  If you need to pipe the output to a pager/file (etc.)
           and still want it prettified, please use an external JSON
           formatter. An example of this:

                dh_assistant supported-compat-levels | json_pp | less

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

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

    14.3                            2026-08-03                DH_ASSISTANT(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh(1)](../man1/dh.1.html),  [debhelper(7)](../man7/debhelper.7.html),  [debhelper-compat-upgrade-checklist(7)](../man7/debhelper-compat-upgrade-checklist.7.html)

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
