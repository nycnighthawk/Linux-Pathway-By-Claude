---
{"title": "yum2dnf(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/yum2dnf.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# yum2dnf(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [\--SKIP-BROKEN](#--SKIP-BROKEN) \| [UPDATE AND UPGRADE COMMANDS ARE THE SAME](#UPDATE_AND_UPGRADE_COMMANDS_ARE_THE_SAME) \| [CLEAN_REQUIREMENTS_ON_REMOVE ON BY DEFAULT](#CLEAN_REQUIREMENTS_ON_REMOVE_ON_BY_DEFAULT) \| [NO RESOLVEDEP COMMAND](#NO_RESOLVEDEP_COMMAND) \| [NO DEPLIST COMMAND](#NO_DEPLIST_COMMAND) \| [EXCLUDES AND REPO EXCLUDES APPLY TO ALL OPERATIONS](#EXCLUDES_AND_REPO_EXCLUDES_APPLY_TO_ALL_OPERATIONS) \| [THE INCLUDE OPTION HAS BEEN REMOVED](#THE_INCLUDE_OPTION_HAS_BEEN_REMOVED) \| [DNF PROVIDES /BIN/\<FILE\> IS NOT FULLY SUPPORTED](#DNF_PROVIDES_/BIN/%3CFILE%3E_IS_NOT_FULLY_SUPPORTED) \| [SKIP_IF_UNAVAILABLE COULD BE ENABLED BY DEFAULT](#SKIP_IF_UNAVAILABLE_COULD_BE_ENABLED_BY_DEFAULT) \| [MIRRORLIST_EXPIRE DROPPED](#MIRRORLIST_EXPIRE_DROPPED) \| [METALINK NOT RECOGNIZED IN THE MIRRORLIST REPO OPTION](#METALINK_NOT_RECOGNIZED_IN_THE_MIRRORLIST_REPO_OPTION) \| [ALWAYSPROMPT DROPPED](#ALWAYSPROMPT_DROPPED) \| [UPGRADE_REQUIREMENTS_ON_INSTALL DROPPED](#UPGRADE_REQUIREMENTS_ON_INSTALL_DROPPED) \| [DNF HISTORY ROLLBACK CHECK DROPPED](#DNF_HISTORY_ROLLBACK_CHECK_DROPPED) \| [PACKAGES REPLACEMENT WITHOUT YUM SWAP](#PACKAGES_REPLACEMENT_WITHOUT_YUM_SWAP) \| [DEPENDENCY PROCESSING DETAILS ARE NOT SHOWN IN THE CLI](#DEPENDENCY_PROCESSING_DETAILS_ARE_NOT_SHOWN_IN_THE_CLI) \| [DNF PROVIDES COMPLIES WITH THE YUM DOCUMENTATION OF THE COMMAND](#DNF_PROVIDES_COMPLIES_WITH_THE_YUM_DOCUMENTATION_OF_THE_COMMAND) \| [BANDWIDTH LIMITING](#BANDWIDTH_LIMITING) \| [INSTALLONLYPKGS CONFIG OPTION](#INSTALLONLYPKGS_CONFIG_OPTION) \| [THE USAGE OF DELTA RPM FILES](#THE_USAGE_OF_DELTA_RPM_FILES) \| [HANDLING .SRPM FILES AND NON-EXISTENT PACKAGES](#HANDLING_.SRPM_FILES_AND_NON-EXISTENT_PACKAGES) \| [PROMOTING PACKAGE TO INSTALL TO A PACKAGE THAT OBSOLETES IT](#PROMOTING_PACKAGE_TO_INSTALL_TO_A_PACKAGE_THAT_OBSOLETES_IT) \| [BEHAVIOR OF \--INSTALLROOT OPTION](#BEHAVIOR_OF_--INSTALLROOT_OPTION) \| [DIFFERENT PROMPT AFTER TRANSACTION TABLE](#DIFFERENT_PROMPT_AFTER_TRANSACTION_TABLE) \| [LIST COMMAND SHOWS ALL REPO ALTERNATIVES](#LIST_COMMAND_SHOWS_ALL_REPO_ALTERNATIVES) \| [YUM-LANGPACKS SUBCOMMANDS HAVE BEEN REMOVED](#YUM-LANGPACKS_SUBCOMMANDS_HAVE_BEEN_REMOVED) \| [FOUND](#FOUND) \| [YUM-UPDATEONBOOT AND YUM-CRON](#YUM-UPDATEONBOOT_AND_YUM-CRON) \| [UTILITIES THAT HAVE NOT BEEN PORTED YET](#UTILITIES_THAT_HAVE_NOT_BEEN_PORTED_YET) \| [Author](#Author) \| [Copyright](#Copyright) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    YUM2DNF(8)                         DNF                         YUM2DNF(8)

## [](#NAME)NAME

           yum2dnf - Changes in DNF compared to YUM

## [](#--SKIP-BROKEN)\--SKIP-BROKEN

           For install command:

           The --skip-broken option is an alias for --setopt=strict=0. Both
           options could be used with DNF to skip all unavailable packages or
           packages with broken dependencies given to DNF without raising an
           error causing the whole operation to fail. This behavior can be
           set as default in dnf.conf file. See strict conf option <#
           strict-label>.

           For upgrade command:

           The semantics that were supposed to trigger in YUM with
           --skip-broken are now set for plain dnf update as a default. There
           is no need to use --skip-broken with the dnf upgrade command. To
           use only the latest versions of packages in transactions, there is
           the --best command line switch.

## [](#UPDATE_AND_UPGRADE_COMMANDS_ARE_THE_SAME)UPDATE AND UPGRADE COMMANDS ARE THE SAME

           Invoking dnf update or dnf upgrade, in all their forms, has the
           same effect in DNF, with the latter being preferred. In YUM yum
           upgrade was exactly like yum --obsoletes update.

## [](#CLEAN_REQUIREMENTS_ON_REMOVE_ON_BY_DEFAULT)CLEAN_REQUIREMENTS_ON_REMOVE ON BY DEFAULT

           The clean_requirements_on_remove <#
           clean-requirements-on-remove-label> switch is on by default in
           DNF. It can thus be confusing to compare the "remove" operation
           results between DNF and YUM as by default DNF is often going to
           remove more packages.

## [](#NO_RESOLVEDEP_COMMAND)NO RESOLVEDEP COMMAND

           The YUM version of this command is maintained for legacy reasons
           only. The user can just use dnf provides to find out what package
           provides a particular file.

## [](#NO_DEPLIST_COMMAND)NO DEPLIST COMMAND

           An alternative to the YUM deplist command to find out dependencies
           of a package is dnf repoquery --deplist using repoquery command <#
           repoquery-command-label>.

           Note:
              Alternatively there is a YUM compatibility support where yum
              deplist is alias for dnf repoquery --deplist command

## [](#EXCLUDES_AND_REPO_EXCLUDES_APPLY_TO_ALL_OPERATIONS)EXCLUDES AND REPO EXCLUDES APPLY TO ALL OPERATIONS

           YUM only respects excludes during installs and upgrades. DNF
           extends this to all operations, among others erasing and listing.
           If you e.g. want to see a list of all installed python-f* packages
           but not any of the Flask packages, the following will work:

              dnf -x '*flask*' list installed 'python-f*'

## [](#THE_INCLUDE_OPTION_HAS_BEEN_REMOVED)THE INCLUDE OPTION HAS BEEN REMOVED

           Inclusion of other configuration files in the main configuration
           file is no longer supported.

## [](#DNF_PROVIDES_/BIN/%3CFILE%3E_IS_NOT_FULLY_SUPPORTED)DNF PROVIDES /BIN/\<FILE\> IS NOT FULLY SUPPORTED

           After UsrMove <https://fedoraproject.org/wiki/Features/UsrMove>
           there's no directory /bin on Fedora systems and no files get
           installed there, /bin is only a symlink created by the filesystem
           package to point to /usr/bin. Resolving the symlinks to their real
           path would only give the user a false sense that this works, while
           in fact provides requests using globs such as:

              dnf provides /b*/<file>

           will fail still (as they do in YUM now). To find what provides a
           particular binary, use the actual path for binaries on Fedora:

              dnf provides /usr/bin/<file>

           Also see related Fedora bugzillas 982947
           <https://bugzilla.redhat.com/show_bug.cgi?id=982947> and 982664
           <https://bugzilla.redhat.com/show_bug.cgi?id=982664>.

## [](#SKIP_IF_UNAVAILABLE_COULD_BE_ENABLED_BY_DEFAULT)SKIP_IF_UNAVAILABLE COULD BE ENABLED BY DEFAULT

           In some distributions DNF is shipped with skip_if_unavailable=True
           in the DNF configuration file <#conf-ref-label>. The reason for
           the change is that third-party repositories can often be
           unavailable. Without this setting in the relevant repository
           configuration file YUM immediately stops on a repository
           synchronization error, confusing and bothering the user.

           See the related Fedora bug 984483
           <https://bugzilla.redhat.com/show_bug.cgi?id=984483>.

    OVERWRITE_GROUPS DROPPED, COMPS FUNCTIONS ACTING AS IF ALWAYS DISABLED
           %%%SH%%%
           This config option has been dropped. When DNF sees several groups
           with the same group ID it merges the groups' contents together.

## [](#MIRRORLIST_EXPIRE_DROPPED)MIRRORLIST_EXPIRE DROPPED

           To simplify things for the user, DNF uses metadata_expire for both
           expiring metadata and the mirrorlist file (which is a kind of
           metadata itself).

## [](#METALINK_NOT_RECOGNIZED_IN_THE_MIRRORLIST_REPO_OPTION)METALINK NOT RECOGNIZED IN THE MIRRORLIST REPO OPTION

           The following part of yum.conf(5) no longer applies for the
           mirrorlist option:
              As a special hack if the mirrorlist URL contains the word
              "metalink" then the value of mirrorlist is copied to metalink
              (if metalink is not set).

           The relevant repository configuration files have been fixed to
           respect this, see the related Fedora bug 948788
           <https://bugzilla.redhat.com/show_bug.cgi?id=948788>.

## [](#ALWAYSPROMPT_DROPPED)ALWAYSPROMPT DROPPED

           Unsupported to simplify the configuration.

## [](#UPGRADE_REQUIREMENTS_ON_INSTALL_DROPPED)UPGRADE_REQUIREMENTS_ON_INSTALL DROPPED

           Dropping this config option with blurry semantics simplifies the
           configuration. DNF behaves as if this was disabled. If the user
           wanted to upgrade everything to the latest version she'd simply
           use dnf upgrade.

## [](#DNF_HISTORY_ROLLBACK_CHECK_DROPPED)DNF HISTORY ROLLBACK CHECK DROPPED

           Since DNF tolerates the use of other package managers, it is
           possible that not all changes to the RPMDB are stored in the
           history of transactions. Therefore, DNF does not fail if such a
           situation is encountered and thus the force option is not needed
           anymore.

## [](#PACKAGES_REPLACEMENT_WITHOUT_YUM_SWAP)PACKAGES REPLACEMENT WITHOUT YUM SWAP

           Time after time one needs to remove an installed package and
           replace it with a different one, providing the same capabilities
           while other packages depending on these capabilities stay
           installed. Without (transiently) breaking consistency of the
           package database this can be done by performing the remove and the
           install in one transaction. The common way to set up such a
           transaction in DNF is to use dnf shell or use the --allowerasing
           switch.

           E.g. say you want to replace A (providing P)  with B (also
           providing P, conflicting with A) without deleting C (which
           requires P) in the process. Use:

              dnf --allowerasing install B

           This command is equal to yum swap A B.

           DNF provides swap command but only dnf swap A B syntax is
           supported

## [](#DEPENDENCY_PROCESSING_DETAILS_ARE_NOT_SHOWN_IN_THE_CLI)DEPENDENCY PROCESSING DETAILS ARE NOT SHOWN IN THE CLI

           During its depsolving phase, YUM outputs lines similar to:

              ---> Package rubygem-rhc.noarch 0:1.16.9-1.fc19 will be an update
              --> Processing Dependency: rubygem-net-ssh-multi >= 1.2.0 for package: rubygem-rhc-1.16.9-1.fc19.noarch

           DNF does not output information like this. The technical reason is
           that depsolver below DNF always considers all dependencies for
           update candidates and the output would be very long. Secondly,
           even in YUM this output gets confusing very quickly especially for
           large transactions and so does more harm than good.

           See the related Fedora bug 1044999
           <https://bugzilla.redhat.com/show_bug.cgi?id=1044999>.

## [](#DNF_PROVIDES_COMPLIES_WITH_THE_YUM_DOCUMENTATION_OF_THE_COMMAND)DNF PROVIDES COMPLIES WITH THE YUM DOCUMENTATION OF THE COMMAND

           When one executes:

              yum provides sandbox

           YUM applies extra heuristics to determine what the user meant by
           sandbox, for instance it sequentially prepends entries from the
           PATH environment variable to it to see if it matches a file
           provided by some package. This is an undocumented behavior that
           DNF does not emulate. Just typically use:

              dnf provides /usr/bin/sandbox

           or even:

              dnf provides '*/sandbox'

           to obtain similar results.

## [](#BANDWIDTH_LIMITING)BANDWIDTH LIMITING

           DNF supports the throttle and bandwidth options familiar from YUM.
           Contrary to YUM, when multiple downloads run simultaneously the
           total downloading speed is throttled. This was not possible in YUM
           since downloaders ran in different processes.

## [](#INSTALLONLYPKGS_CONFIG_OPTION)INSTALLONLYPKGS CONFIG OPTION

           Compared to YUM, DNF appends list values from the installonlypkgs
           config option to DNF defaults, where YUM overwrites the defaults
           by option values.

## [](#THE_USAGE_OF_DELTA_RPM_FILES)THE USAGE OF DELTA RPM FILES

           The boolean deltarpm option controls whether delta RPM files are
           used. Compared to YUM, DNF does not support deltarpm_percentage
           and instead chooses some optimal value of DRPM/RPM ratio to decide
           whether using deltarpm makes sense in the given case.

## [](#HANDLING_.SRPM_FILES_AND_NON-EXISTENT_PACKAGES)HANDLING .SRPM FILES AND NON-EXISTENT PACKAGES

           DNF will terminate early with an error if a command is executed
           requesting an installing operation on a local .srpm file:

              $ dnf install fdn-0.4.17-1.fc20.src.rpm tour-4-6.noarch.rpm
              Error: Will not install a source rpm package (fdn-0.4.17-1.fc20.src).

           The same applies for package specifications that do not match any
           available package.

           YUM will only issue a warning in this case and continue installing
           the "tour" package. The rationale behind the result in DNF is that
           a program should terminate with an error if it can not fulfill the
           CLI command in its entirety.

## [](#PROMOTING_PACKAGE_TO_INSTALL_TO_A_PACKAGE_THAT_OBSOLETES_IT)PROMOTING PACKAGE TO INSTALL TO A PACKAGE THAT OBSOLETES IT

           DNF will not magically replace a request for installing package X
           to installing package Y if Y obsoletes X. YUM does this if its
           obsoletes config option is enabled but the behavior is not
           properly documented and can be harmful.

           See the related Fedora bug 1096506
           <https://bugzilla.redhat.com/show_bug.cgi?id=1096506> and
           guidelines for renaming and obsoleting packages in Fedora
           <http://fedoraproject.org/wiki/Upgrade_paths_%E2%80%94_renaming_or_splitting_packages>.

## [](#BEHAVIOR_OF_--INSTALLROOT_OPTION)BEHAVIOR OF \--INSTALLROOT OPTION

           DNF offers more predictable behavior of installroot. DNF handles
           the path differently from the --config command-line option, where
           this path is always related to the host system (YUM combines this
           path with installroot). Reposdir is also handled slightly
           differently, if one path of the reposdirs exists inside of
           installroot, then repos are strictly taken from installroot (YUM
           tests each path from reposdir separately and use installroot path
           if existed). See the detailed description for --installroot <#
           installroot-label> option.

## [](#DIFFERENT_PROMPT_AFTER_TRANSACTION_TABLE)DIFFERENT PROMPT AFTER TRANSACTION TABLE

           DNF doesn't provide download functionality after displaying
           transaction table. It only asks user whether to continue with
           transaction or not.  If one wants to download packages, they can
           use the 'download' command.

## [](#LIST_COMMAND_SHOWS_ALL_REPO_ALTERNATIVES)LIST COMMAND SHOWS ALL REPO ALTERNATIVES

           DNF lists all packages from all repos, which means there can be
           duplicates package names (with different repo name). This is due
           to providing users possibility to choose preferred repo.

## [](#YUM-LANGPACKS_SUBCOMMANDS_HAVE_BEEN_REMOVED)YUM-LANGPACKS SUBCOMMANDS HAVE BEEN REMOVED

           Translations became part of core DNF and it is no longer necessary
           to manage individual language packs.

           Following sub-commands were removed:

           • langavailable

           • langinstall

           • langremove

           • langlist

           • langinfo

    DNF HISTORY SUBCOMMANDS LIST AND INFO RETURN 0 WHEN TRANSACTIONS NOT

## [](#FOUND)FOUND

           DNF dnf history list and dnf history info return a zero exit
           status when they fail to find transactions for a specified
           package.

           This is different from corresponding YUM yum history package-list
           and yum history list, which both return a non-zero exit status
           when they fail to find
              transactions for a specified package.
    ┌─────────────────────────────────────┬───────────────────────────────────────────────────────────────┬────────────────────────────────┐
    │ Original YUM tool                   │ DNF command/option                                            │ Package                        │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum check                           │ dnf repoquery <#                                              │ dnf                            │
    │                                     │ repoquery-command-                                            │                                │
    │                                     │ label>                                                        │                                │
    │                                     │ --unsatisfied                                                 │                                │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-langpacks                       │                                                               │ dnf                            │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-aliases                  │ dnf alias <#                                                  │ dnf                            │
    │                                     │ alias-command-                                                │                                │
    │                                     │ label>                                                        │                                │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-auto-update-debug-info   │ option in                                                     │ dnf-plugins-core               │
    │                                     │ debuginfo-install.conf                                        │                                │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-changelog                │                                                               │ dnf-plugins-core               │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-copr                     │ dnf copr                                                      │ dnf-plugins-core               │
    │                                     │ <https://dnf-plugins-core.readthedocs.io/en/latest/copr.html> │                                │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-fastestmirror            │ fastestmirror option in dnf.conf                              │ dnf                            │
    │                                     │ <https://dnf.readthedocs.io/en/latest/conf_ref.html>          │                                │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-fs-snapshot              │                                                               │ dnf-plugins-extras-snapper     │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-local                    │                                                               │ dnf-plugins-core               │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-merge-conf               │                                                               │ dnf-plugins-extras-rpmconf     │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-post-transaction-actions │                                                               │ dnf-plugins-core               │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-priorities               │ priority option in dnf.conf                                   │ dnf                            │
    │                                     │ <https://dnf.readthedocs.io/en/latest/conf_ref.html>          │                                │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-remove-with-leaves       │ dnf autoremove <#autoremove-command-label>                    │ dnf                            │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-show-leaves              │                                                               │ dnf-plugins-core               │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-tmprepo                  │ --repofrompath option                                         │ dnf                            │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-tsflags                  │ tsflags  option in dnf.conf                                   │ dnf                            │
    │                                     │ <https://dnf.readthedocs.io/en/latest/conf_ref.html>          │                                │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-plugin-versionlock              │                                                               │ python3-dnf-plugin-versionlock │
    ├─────────────────────────────────────┼───────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-rhn-plugin                      │                                                               │ dnf-plugin-spacewalk           │
    └─────────────────────────────────────┴───────────────────────────────────────────────────────────────┴────────────────────────────────┘

           Plugins that have not been ported yet:

           yum-plugin-filter-data, yum-plugin-keys, yum-plugin-list-data,
           yum-plugin-protectbase, yum-plugin-ps, yum-plugin-puppetverify,
           yum-plugin-refresh-updatesd, yum-plugin-rpm-warm-cache,
           yum-plugin-upgrade-helper, yum-plugin-verify

           Feel free to file an RFE
           <https://github.com/rpm-software-management/dnf/wiki/Bug-Reporting#new-feature-request>
           for missing functionality if you need it.

           All ported YUM tools are now implemented as DNF plugins.
    ┌───────────────────────┬────────────────────────────────────────────────────────────────────────────┬────────────────────────────────┐
    │ Original YUM tool     │ New DNF command                                                            │ Package                        │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ debuginfo-install     │ dnf                                                                        │ dnf-plugins-core               │
    │                       │ debuginfo-install                                                          │                                │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/debuginfo-install.html> │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ find-repos-of-install │ dnf list installed <https://dnf.readthedocs.io/en/latest/command_ref.html> │ dnf                            │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ needs-restarting      │ dnf tracer                                                                 │ dnf-plugins-extras-tracer      │
    │                       │ <https://dnf-plugins-extras.readthedocs.io/en/latest/tracer.html>          │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ package-cleanup       │ dnf list <#list-command-label>, dnf repoquery <#repoquery-command-label>   │ dnf, dnf-plugins-core          │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ repoclosure           │ dnf repoclosure                                                            │ dnf-plugins-extras-repoclosure │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/repoclosure.html>       │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ repodiff              │ dnf repodiff                                                               │ dnf-plugins-core               │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/repodiff.html>          │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ repo-graph            │ dnf repograph                                                              │ dnf-plugins-extras-repograph   │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/repograph.html>         │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ repomanage            │ dnf repomanage                                                             │ dnf-plugins-extras-repomanage  │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/repomanage.html>        │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ repoquery             │ dnf repoquery <#repoquery-command-label>                                   │ dnf                            │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ reposync              │ dnf reposync                                                               │ dnf-plugins-core               │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/reposync.html>          │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ repotrack             │ dnf download                                                               │ dnf-plugins-core               │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>          │                                │
    │                       │ --resolve --alldeps                                                        │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-builddep          │ dnf builddep                                                               │ dnf-plugins-core               │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/builddep.html>          │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-config-manager    │ dnf config-manager                                                         │ dnf-plugins-core               │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/config_manager.html>    │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-debug-dump        │ dnf debug-dump                                                             │ dnf-plugins-extras-debug       │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/debug.html>             │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yum-debug-restore     │ dnf debug-restore                                                          │ dnf-plugins-extras-debug       │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/debug.html>             │                                │
    ├───────────────────────┼────────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
    │ yumdownloader         │ dnf download                                                               │ dnf-plugins-core               │
    │                       │ <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>          │                                │
    └───────────────────────┴────────────────────────────────────────────────────────────────────────────┴────────────────────────────────┘

           Detailed table for package-cleanup replacement:
                ┌──────────────────────────┬──────────────────────────┐
                │ package-cleanup --dupes  │ dnf repoquery            │
                │                          │ --duplicates             │
                ├──────────────────────────┼──────────────────────────┤
                │ package-cleanup --leaves │ dnf repoquery --unneeded │
                ├──────────────────────────┼──────────────────────────┤
                │ package-cleanup          │ dnf repoquery --extras   │
                │ --orphans                │                          │
                ├──────────────────────────┼──────────────────────────┤
                │ package-cleanup          │ dnf repoquery            │
                │ --problems               │ --unsatisfied            │
                ├──────────────────────────┼──────────────────────────┤
                │ package-cleanup          │ dnf remove --duplicates  │
                │ --cleandupes             │                          │
                ├──────────────────────────┼──────────────────────────┤
                │ package-cleanup          │ dnf remove               │
                │ --oldkernels             │ --oldinstallonly         │
                ├──────────────────────────┼──────────────────────────┤
                │ package-cleanup          │ dnf remove $(dnf         │
                │ --oldkernels --keep=2    │ repoquery --installonly  │
                │                          │ --latest-limit=-2)       │
                └──────────────────────────┴──────────────────────────┘

## [](#YUM-UPDATEONBOOT_AND_YUM-CRON)YUM-UPDATEONBOOT AND YUM-CRON

           DNF does not have a direct replacement of yum-updateonboot and
           yum-cron commands.  However, the similar result can be achieved by
           dnf automatic command (see DNF Automatic <>).

           You can either use the shortcut:

              $ systemctl enable --now dnf-automatic-install.timer

           Or set apply_updates option of /etc/dnf/automatic.conf to True and
           use generic timer unit:

              $ systemctl enable --now dnf-automatic.timer

           The timer in both cases is activated 1 hour after the system was
           booted up and then repetitively once every 24 hours. There is also
           a random delay on these timers set to 5 minutes. These values can
           be tweaked via dnf-automatic*.timer config files located in the
           /usr/lib/systemd/system/ directory.

## [](#UTILITIES_THAT_HAVE_NOT_BEEN_PORTED_YET)UTILITIES THAT HAVE NOT BEEN PORTED YET

           repo-rss, show-changed-rco, show-installed, verifytree,
           yum-groups-manager

           Take a look at the FAQ
           <https://dnf.readthedocs.io/en/latest/user_faq.html> about YUM to
           DNF migration. Feel free to file an RFE
           <https://github.com/rpm-software-management/dnf/wiki/Bug-Reporting#new-feature-request>
           for missing functionality if you need it.

## [](#Author)Author

           See AUTHORS in DNF source distribution.

## [](#Copyright)Copyright

           2012-2020, Red Hat, Licensed under GPLv2+

## [](#COLOPHON)COLOPHON

           This page is part of the dnf (DNF Package Manager) project.
           Information about the project can be found at 
           ⟨https://github.com/rpm-software-management/dnf⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           project's upstream Git repository
           ⟨https://github.com/rpm-software-management/dnf.git⟩ on
           2026-08-03.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-13.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    4.25.0                         Aug 03, 2026                    YUM2DNF(8)

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
