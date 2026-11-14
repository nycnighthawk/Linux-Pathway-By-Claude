---
{"title": "dh(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/dh.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dh(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OVERRIDE AND HOOK TARGETS](#OVERRIDE_AND_HOOK_TARGETS) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [DEBHELPER PROVIDED DH ADDONS](#DEBHELPER_PROVIDED_DH_ADDONS) \| [INTERNALS](#INTERNALS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                     |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DH(1)                           Debhelper                           DH(1)

## [](#NAME)NAME

           dh - debhelper command sequencer

## [](#SYNOPSIS)SYNOPSIS

           dh sequence [--with addon[,addon ...]] [--list]
           [debhelper options]

## [](#DESCRIPTION)DESCRIPTION

           dh runs a sequence of debhelper commands. The supported sequences
           correspond to the targets of a debian/rules file: build-arch,
           build-indep, build, clean, install-indep, install-arch, install,
           binary-arch, binary-indep, and binary.

## [](#OVERRIDE_AND_HOOK_TARGETS)OVERRIDE AND HOOK TARGETS

           A debian/rules file using dh can override the command that is run
           at any step in a sequence, by defining an override target.  It is
           also possible to inject a command before or after any step without
           affecting the step itself.

       Injecting commands before or after a step
           Note: This feature requires debhelper 12.8 or later plus the
           package must use compatibility mode 10 or later.

           To inject commands before dh_command, add a target named
           execute_before_dh_command to the rules files.  Similarly, if you
           want to inject commands after dh_command, add the target
           execute_after_dh_command.  Both targets can be used for the same
           dh_command and also even if the command is overridden (as
           described in "Overriding a command" below).

           When these targets are defined, dh will call the targets
           respectively before or after it would invoke dh_command (or its
           override target).

       Overriding a command
           To override dh_command, add a target named override_dh_command to
           the rules file. When it would normally run dh_command, dh will
           instead call that target. The override target can then run the
           command with additional options, or run entirely different
           commands instead. See examples below.

           As of debhelper version 13.25, override targets (but not other
           hook targets) can use the $(DH_OVERRIDDEN_COMMAND) makefile
           variable to run the command being overridden exactly as it was.
           This can be useful if you want to add extra options like:

               # These examples require debhelper/13.25 or later
               override_dh_auto_configure:
                   $(DH_OVERRIDDEN_COMMAND) -- --with-foo --with-bar

               override_dh_auto_test:
                   fakeroot $(DH_OVERRIDDEN_COMMAND)

           Note this variable is only useful if you want to run the original
           command with something extra. If you just want to run the original
           command with no changes, use execute_before_dh_foo or/and
           execute_after_dh_foo instead.

           Be careful with this variable. In older versions of debhelper, the
           variable is unset, which will cause it to expand to nothing.
           Depending on what else is on the line, this may not cause a
           failure where you expect it.

           Additionally, be careful with typos. English has a grammatical
           irregularity here, where override has one d (target name;
           imperative) whereas the OVERRIDDEN has two Ds (variable name; past
           particle).  It is unfortunate and confusing, but that is how
           English grammar works.

       Architecture dependent/independent override and hook targets
           The override and hook targets can also be defined to run only when
           building architecture dependent or architecture independent
           packages. Use targets with names like override_dh_command-arch and
           execute_after_dh_command-indep.

           This feature is available since debhelper 8.9.7 (for override
           targets) and 12.8 (for hook targets).

       Completely empty targets
           As a special optimization, dh will skip a target if it is
           completely empty and does not depend on any other target.  This is
           mostly useful for override targets, where the command will simply
           be skipped without the overhead of invoking a dummy target.

           Note that the target has to be completely empty for this to work:

                # Skip dh_bar - the good and optimized way
                # Some rationale for skipping dh_bar goes here
                override_dh_bar:

                # Skip dh_foo - the slow way
                override_dh_foo:
                   # Some rationale for skipping dh_foo goes here
                   # (these comments causes a dummy target to be run)

       Verifying targets are picked up by dh
           As of debhelper 13.10, you can use dh_assistant(1) to see which
           override and hook targets will be seen by dh.  Here is an example
           run of dh_assistant(1) along with its output:

               $ dh_assistant detect-hook-targets
               {
                  "commands-not-in-path": [
                     "dh_foo"
                  ],
                  "hook-targets": [
                     {
                        "command": "dh_strip_nondeterminism",
                        "is-empty": true,
                        "package-section-param": null,
                        "target-name": "override_dh_strip_nondeterminism"
                     },
                     {
                        "command": "dh_foo",
                        "is-empty": false,
                        "package-section-param": "-a",
                        "target-name": "override_dh_foo-arch"
                     }
                  ]
               }

           The commands-not-in-path is useful for spotting mistakes in the
           hook target names.  A non-empty value implies one of more hook
           targets are related to a command that is either not installed or
           no command with that name exists at all.  It is generally worth
           double checking these.

           Additionally, the is-empty attribute for each hook target can be
           used for seeing whether a hook target triggers the "Completely
           empty targets" optimization.

           If you are interested in the other attributes, please read the
           dh_assistant(1) for the details.

           Verifying targets are picked up by dh (when debhelper is older
           than 13.10)

           On older versions of debhelper, you have to use dh with --no-act.
           You can use the following command as an example:

               $ dh binary --no-act | grep dh_install | head -n5
                    dh_installdirs
                    dh_install
                    debian/rules execute_after_dh_install
                    dh_installdocs
                    dh_installchangelogs

           The debian/rules execute_after_dh_install in the output, which
           signals that dh registered a execute_after_dh_install target and
           would run it directly after dh_install(1).

           Note that "Completely empty targets" will be omitted in the
           listing above.  This makes it a bit harder to spot as you are
           looking for the omission of a command name.  But otherwise, the
           principle remains the same.

       Caveats with hook targets and makefile conditionals
           If you choose to wrap a hook target in makefile conditionals,
           please be aware that dh computes all the hook targets ahead of
           time and caches the result for that run.  Furthermore, the
           conditionals will be invoked again when dh calls the hook target
           later and will assume the answer did not change.

           The parsing and caching often happens before dh knows whether it
           will build arch:any (-a) or/and arch:all (-i) packages, which can
           produce confusing results - especially when dh_listpackages(1) is
           part of the conditional.

           Most of the problems can be avoided by making the hook target
           unconditional and then have the "body" be partially or completely
           conditional.  As an example:

                 # SIMPLE: It is well-defined what happens.  The hook target
                 # is always considered.  The "maybe run this" bit is
                 # conditional but dh_foo is definitely skipped.
                 #
                 # Note: The conditional is evaluated "twice" where its
                 # influences what happens.  Once when dh check which hook
                 # targets exist and once when the override_dh_foo hook target
                 # is run.  If *either* times return false, "maybe run this"
                 # is skipped.
                 override_dh_foo:
                 ifneq (...)
                     maybe run this
                 endif

                 # SIMPLE: This is also well-defined.  The hook target is always
                 # run and dh_bar is skipped.  The "maybe run this" bit is
                 # conditional as one might expect.
                 #
                 # Note: The conditional is still evaluated multiple times (in
                 # different process each time).  However, only the evaluation
                 # that happens when the hook target is run influences what
                 # happens.
                 override_dh_bar:
                     : # Dummy command to force the target to always be run
                 ifneq (...)
                     maybe run this
                 endif

                 # COMPLICATED: This case can be non-trivial and have sharp edges.
                 # Use at your own peril if dh_listpackages in the conditional.
                 #
                 # Here, either dh_baz is run normally OR "maybe run this" is run
                 # instead.
                 #
                 # And it gets even more complicated to reason about if dh needs to
                 # recurse into debian/rules because you have an "explicit"
                 # standard target (e.g. a "build-arch:" target separate from "%:").
                 ifneq (...)
                 override_dh_baz:
                     maybe run this
                 endif

           These recipes are also relevant for conditional dependency
           targets, which are often seen in a variant of the following
           example:

                 COND_TASKS =
                 ifneq (...)
                 COND_TASKS += maybe-run-this
                 endif
                 ...

                 maybe-run-this:
                     ...

                 # SIMPLE: It is well-defined what happens.  Either the
                 # $(COND_TASKS) are skipped or run.
                 #
                 # Note: The conditional is evaluated "twice" where its
                 # influences what happens.  Once when dh check which hook
                 # targets exist and once when the override_dh_foo hook target
                 # is run.  If *either* times return false, $(COND_TASKS)
                 # is skipped.
                 override_dh_foo: $(COND_TASKS)

                 # SIMPLE: This is also well-defined.  The hook target is always
                 # run and dh_bar is skipped.  The $(COND_TASKS) bit is
                 # conditional as one might expect.
                 #
                 # Note: The conditional is still evaluated multiple times (in
                 # different process each time).  However, only the evaluation
                 # that happens when the hook target is run influences what
                 # happens.
                 override_dh_bar: $(COND_TASKS)
                     : # Dummy command to force the target to always be run

                 # COMPLICATED: This case can be non-trivial and have sharp edges.
                 # Use at your own peril if dh_listpackages in the conditional.
                 #
                 ifneq (...)
                 override_dh_baz: $(COND_TASKS)
                 endif

           When in doubt, pick the relevant SIMPLE case in the examples above
           that match your need.

## [](#OPTIONS)OPTIONS

           --with addon[,addon ...]
               Add the debhelper commands specified by the given addon to
               appropriate places in the sequence of commands that is run.
               This option can be repeated more than once, or multiple addons
               can be listed, separated by commas.  This is used when there
               is a third-party package that provides debhelper commands. See
               the PROGRAMMING file for documentation about the sequence
               addon interface.

               A Build-Depends relation on the package dh-sequence-addon
               implies a --with addon. This avoids the need for an explicit
               --with in debian/rules that only duplicates what is already
               declared via the build dependencies in debian/control.  The
               relation can (since 12.5) be made optional via e.g.
               build-profiles.  This enables you to easily disable an addon
               that is only useful with certain profiles (e.g. to facilitate
               bootstrapping).

               Since debhelper 12.5, addons can also be activated in
               indep-only mode (via Build-Depends-Indep) or arch-only mode
               (via Build-Depends-Arch). Such addons are only active in the
               particular sequence (e.g. binary-indep) which simplifies
               dependency management for cross-builds.

               Please note that addons activated via Build-Depends-Indep or
               Build-Depends-Arch are subject to additional limitations to
               ensure the result is deterministic even when the addon is
               unavailable (e.g. during clean).  This implies that some
               addons are incompatible with these restrictions and can only
               be used via Build-Depends (or manually via debian/rules).
               Currently, such addons can only add commands to sequences.

           --without addon
               The inverse of --with, disables using the given addon. This
               option can be repeated more than once, or multiple addons to
               disable can be listed, separated by commas.

           --list, -l
               List all available addons.

               When called only with this option, dh can be called from any
               directory (i.e. it does not need access to files from a source
               package).

           --no-act
               Prints commands that would run for a given sequence, but does
               not run them.

               Note that dh normally skips running commands that it knows
               will do nothing.  With --no-act, the full list of commands in
               a sequence is printed.

           Other options passed to dh are passed on to each command it runs.
           This can be used to set an option like -v or -X or -N, as well as
           for more specialised options.

## [](#EXAMPLES)EXAMPLES

           To see what commands are included in a sequence, without actually
           doing anything:

                   dh binary-arch --no-act

           This is a very simple rules file, for packages where the default
           sequences of commands work with no additional options.

                   #!/usr/bin/make -f
                   %:
                           dh $@

           Often you'll want to pass an option to a specific debhelper
           command. The easy way to do with is by adding an override target
           for that command.

                   #!/usr/bin/make -f
                   %:
                           dh $@

                   override_dh_strip:
                           dh_strip -Xfoo

                   override_dh_auto_configure:
                           dh_auto_configure -- --with-foo --disable-bar

           Sometimes the automated dh_auto_configure(1) and dh_auto_build(1)
           can't guess what to do for a strange package. Here's how to avoid
           running either and instead run your own commands.

                   #!/usr/bin/make -f
                   %:
                           dh $@

                   override_dh_auto_configure:
                           ./mondoconfig

                   override_dh_auto_build:
                           make universe-explode-in-delight

           Another common case is wanting to do something manually before or
           after a particular debhelper command is run.

                   #!/usr/bin/make -f
                   %:
                           dh $@

                   # Example assumes debhelper/12.8 and compat 10+
                   execute_after_dh_fixperms:
                           chmod 4755 debian/foo/usr/bin/foo

           If you are on an older debhelper or compatibility level, the above
           example would have to be written as.

                   #!/usr/bin/make -f
                   %:
                           dh $@

                   # Older debhelper versions or using compat 9 or lower.
                   override_dh_fixperms:
                           dh_fixperms
                           chmod 4755 debian/foo/usr/bin/foo

           Python tools are not run by dh by default, due to the continual
           change in that area. Here is how to use dh_python2.

                   #!/usr/bin/make -f
                   %:
                           dh $@ --with python2

           Here is how to force use of Perl's Module::Build build system,
           which can be necessary if debhelper wrongly detects that the
           package uses MakeMaker.

                   #!/usr/bin/make -f
                   %:
                           dh $@ --buildsystem=perl_build

           Here is an example of overriding where the dh_auto_* commands find
           the package's source, for a package where the source is located in
           a subdirectory.

                   #!/usr/bin/make -f
                   %:
                           dh $@ --sourcedirectory=src

           And here is an example of how to tell the dh_auto_* commands to
           build in a subdirectory, which will be removed on clean.

                   #!/usr/bin/make -f
                   %:
                           dh $@ --builddirectory=build

           If your package can be built in parallel, please either use compat
           10 or pass --parallel to dh. Then dpkg-buildpackage -j will work.

                   #!/usr/bin/make -f
                   %:
                           dh $@ --parallel

           If your package cannot be built reliably while using multiple
           threads, please pass --no-parallel to dh (or the relevant
           dh_auto_* command):

                   #!/usr/bin/make -f
                   %:
                           dh $@ --no-parallel

           Here is a way to prevent dh from running several commands that you
           don't want it to run, by defining empty override targets for each
           command.

                   #!/usr/bin/make -f
                   %:
                           dh $@

                   # Commands not to run:
                   override_dh_auto_test override_dh_compress override_dh_fixperms:

           A long build process for a separate documentation package can be
           separated out using architecture independent overrides.  These
           will be skipped when running build-arch and binary-arch sequences.

                   #!/usr/bin/make -f
                   %:
                           dh $@

                   override_dh_auto_build-indep:
                           $(MAKE) -C docs

                   # No tests needed for docs
                   override_dh_auto_test-indep:

                   override_dh_auto_install-indep:
                           $(MAKE) -C docs install

           Adding to the example above, suppose you need to chmod a file, but
           only when building the architecture dependent package, as it's not
           present when building only documentation.

                   # Example assumes debhelper/12.8 and compat 10+
                   execute_after_dh_fixperms-arch:
                           chmod 4755 debian/foo/usr/bin/foo

## [](#DEBHELPER_PROVIDED_DH_ADDONS)DEBHELPER PROVIDED DH ADDONS

           The primary purpose of dh addons is to provide easy integration
           with third-party provided features for debhelper.  However,
           debhelper itself also provide a few sequences that can be useful
           in some cases.  These are documented in this list:

           build-stamp
               A special addon for controlling whether dh (in compat 10 or
               later) will create stamp files to tell whether the build
               target has been run successfully. See "INTERNALS" for more
               details.

               This addon is active by default but can disabled by using dh
               $@ --without build-stamp

           dwz Adds dh_dwz(1) to the sequence.

               Note this is only relevant in compats below 11 or in compat
               14+. It was on by default in compat 12 and 13.

           elf-tools
               This addon adds tools related to ELF files to the sequence
               such as dh_strip(1) and dh_shlibdeps(1)

               This addon is conditionally active by default for architecture
               specific packages - that is, it is skipped for arch:all
               packages.  In the special case where you need these tools to
               work on arch:all packages, you can use --with elf-tools to
               activate it unconditionally.

           installinitramfs (obsolete)
               Adds dh_installinitramfs(1) to the sequence in compat level 11
               or below.  Obsolete in compat 12 or later.

           root-sequence (internal)
               This is reserved for internal usage.

           single-binary
               A special-purpose addon that makes debhelper run in "single
               binary" mode.

               When active, it will pass --destdir=debian/package/ to
               dh_auto_install(1).  This makes every file "installed" by the
               upstream build system part of the (only) binary package by
               default without having to use other helpers such as
               dh_install(1).

               The addon will refuse to activate when the source package
               lists 2 or more binary packages in debian/control as a
               precaution.

               Before compat 15. this behaviour was the default when there
               was only a single binary package listed in debian/control.  In
               compat 15 and later, this addon must explicitly be activated
               for this feature to work.

               The rationale for requiring this as an explicit choice is that
               if it is implicit then debhelper will silently change
               behaviour on adding a new binary package.  This has caused
               many RC bugs when maintainers renamed a binary and added
               transitional packages with the intention of supporting
               seamless upgrades.  The result would often be two empty binary
               packages that were uploaded to archive with users frustrated
               as their "upgrade" removed their programs.

           systemd (obsolete)
               Adds dh_systemd_enable(1) and dh_systemd_start(1) to the
               sequence in compat level 10 or below.  Obsolete in compat 11
               or later.

## [](#INTERNALS)INTERNALS

           If you're curious about dh's internals, here's how it works under
           the hood.

           In compat 10 (or later), dh creates a stamp file
           debian/debhelper-build-stamp after the build step(s) are complete
           to avoid re-running them.  It is possible to avoid the stamp file
           by passing --without=build-stamp to dh.  This makes "no clean"
           builds behave more like what some people expect at the expense of
           possibly running the build and test twice (the second time as root
           or under fakeroot(1)).

           Inside an override target, dh_* commands will create a log file
           debian/package.debhelper.log to keep track of which packages the
           command(s) have been run for.  These log files are then removed
           once the override target is complete.

           In compat 9 or earlier, each debhelper command will record when
           it's successfully run in debian/package.debhelper.log. (Which
           dh_clean deletes.) So dh can tell which commands have already been
           run, for which packages, and skip running those commands again.

           Each time dh is run (in compat 9 or earlier), it examines the log,
           and finds the last logged command that is in the specified
           sequence. It then continues with the next command in the sequence.

           A sequence can also run dependent targets in debian/rules.  For
           example, the "binary" sequence runs the "install" target.

           dh uses the DH_INTERNAL_OPTIONS environment variable to pass
           information through to debhelper commands that are run inside
           override targets. The contents (and indeed, existence) of this
           environment variable, as the name might suggest, is subject to
           change at any time.

           Commands in the build-indep, install-indep and binary-indep
           sequences are passed the -i option to ensure they only work on
           architecture independent packages, and commands in the build-arch,
           install-arch and binary-arch sequences are passed the -a option to
           ensure they only work on architecture dependent packages.

## [](#SEE_ALSO)SEE ALSO

           debhelper(7)

           This program is a part of debhelper.

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

    13.31                           2026-05-24                          DH(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_assistant(1)](../man1/dh_assistant.1.html),  [dh_auto_install(1)](../man1/dh_auto_install.1.html),  [debhelper(7)](../man7/debhelper.7.html)

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
