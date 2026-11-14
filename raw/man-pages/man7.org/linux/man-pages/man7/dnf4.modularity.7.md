---
{"title": "dnf4.modularity(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/dnf4.modularity.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dnf4.modularity(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DEFINITIONS](#DEFINITIONS) \| [PACKAGE FILTERING](#PACKAGE_FILTERING) \| [ADVISORY FILTERING](#ADVISORY_FILTERING) \| [HOTFIX REPOSITORIES](#HOTFIX_REPOSITORIES) \| [FAIL-SAFE MECHANISMS](#FAIL-SAFE_MECHANISMS) \| [Author](#Author) \| [Copyright](#Copyright) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DNF4.MODULARITY(7)                 DNF                 DNF4.MODULARITY(7)

## [](#NAME)NAME

           dnf4.modularity - Modularity in DNF

           Warning:
              Modularity is deprecated, and functionality will be removed in
              a future release of DNF5.

           Modularity is new way of building, organizing and delivering
           packages.  For more details see:
           <https://docs.pagure.org/modularity/>

## [](#DEFINITIONS)DEFINITIONS

           modulemd
                  Every repository can contain modules metadata with modulemd
                  documents.  These documents hold metadata about modules
                  such as Name, Stream or list of packages.

           (non-modular) package
                  Package that doesn't belong to a module.

           modular package
                  Package that belongs to a module. It is listed in modulemd
                  under the artifacts section.  Modular packages can be also
                  identified by having %{modularitylabel} RPM header set.

           (module) stream
                  Stream is a collection of packages, a virtual repository.
                  It is identified with Name and Stream from modulemd
                  separated with colon, for example "postgresql:9.6".

                  Module streams can be active or inactive. active means the
                  RPM packages from this stream are included in the set of
                  available packages.  Packages from inactive streams are
                  filtered out.  Streams are active either if marked as
                  default or if they are explicitly enabled by a user action.
                  Streams that satisfy dependencies of default or enabled
                  streams are also considered active.  Only one stream of a
                  particular module can be active at a given point in time.

## [](#PACKAGE_FILTERING)PACKAGE FILTERING

           Without modules, packages with the highest version are used by
           default.

           Module streams can distribute packages with lower versions than
           available in the repositories available to the operating system.
           To make such packages available for installs and upgrades, the
           non-modular packages are filtered out when their name or provide
           matches against a modular package name from any enabled, default,
           or dependent stream. Modular source packages will not cause
           non-modular binary packages to be filtered out.

## [](#ADVISORY_FILTERING)ADVISORY FILTERING

           When modular package filtering is active, update advisories for
           non-modular versions of packages governed by an active module
           stream are also filtered out.  This prevents displaying advisories
           that cannot be acted upon because the corresponding packages are
           excluded by modular filtering.

           The filtering matches advisory packages against the set of
           module-excluded packages. Advisories referencing packages not
           present in any enabled repository (e.g. older versions no longer
           available in repositories) cannot be matched and may still be
           displayed even though the packages are not installable.

       Demodularized rpms
           Contains names of RPMs excluded from package filtering for
           particular module stream. When defined in the latest active
           module, non-modular RPMs with the same name or provide which were
           previously filtered out will reappear.

## [](#HOTFIX_REPOSITORIES)HOTFIX REPOSITORIES

           In special cases, a user wants to cherry-pick individual packages
           provided outside module streams and make them available on along
           with packages from the active streams.  Under normal
           circumstances, such packages are filtered out or rejected from
           getting on the system by Fail-safe mechanisms.  To make the system
           use packages from a repository regardless of their modularity,
           specify module_hotfixes=true in the .repo file. This protects the
           repository from package filtering.

           Please note the hotfix packages do not override module packages,
           they only become part of available package set. It's the package
           Epoch, Version and Release what determines if the package is the
           latest.

## [](#FAIL-SAFE_MECHANISMS)FAIL-SAFE MECHANISMS

       Repositories with module metadata are unavailable
           When a repository with module metadata is unavailable, package
           filtering must keep working.  Non-modular RPMs must remain
           unavailable and must never get on the system.

           This happens when:

           • user disables a repository via --disablerepo or uses --repoid

           • user removes a .repo file from disk

           • repository is not available and has skip_if_unavailable=true

           DNF keeps copies of the latest modulemd for every active stream
           and uses them if there's no modulemd available for the stream.
           This keeps package filtering working correctly.

           The copies are made any time a transaction is resolved and
           started.  That includes RPM transactions as well as any dnf module
           <enable|disable|reset> operations.

           When the fail-safe data is used, dnf show such modules as part of
           @modulefailsafe repository.

       Orphaned modular packages
           All packages that are built as a part of a module have
           %{modularitylabel} RPM header set.  If such package becomes part
           of RPM transaction and cannot be associated with any available
           modulemd, DNF prevents from getting it on the system (package is
           available, but cannot be installed, upgraded, etc.). Packages from
           Hotfix repositories or Commandline repository are not affected by
           Fail-safe mechanisms.

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

    4.25.0                         Aug 03, 2026            DNF4.MODULARITY(7)

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
