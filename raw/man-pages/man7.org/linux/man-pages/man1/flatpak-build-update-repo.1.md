---
{"title": "flatpak-build-update-repo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-build-update-repo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-build-update-repo(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK BUILD-UPDAT(1)  flatpak build-update-repo  FLATPAK BUILD-UPDAT(1)

## [](#NAME)NAME

           flatpak-build-update-repo - Create a repository from a build
           directory

## [](#SYNOPSIS)SYNOPSIS

           flatpak build-update-repo [OPTION...] LOCATION

## [](#DESCRIPTION)DESCRIPTION

           Updates repository metadata for the repository at LOCATION. This
           command generates an OSTree summary file that lists the contents
           of the repository. The summary is used by flatpak remote-ls and
           other commands to display the contents of remote repositories.

           After this command, LOCATION can be used as the repository
           location for flatpak remote-add, either by exporting it over http,
           or directly with a file: url.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --redirect-url=URL
               Redirect this repo to a new URL.

           --title=TITLE
               A title for the repository, e.g. for display in a UI. The
               title is stored in the repository summary.

           --comment=COMMENT
               A single-line comment for the remote, e.g. for display in a
               UI. The comment is stored in the repository summary.

           --description=DESCRIPTION
               A full-paragraph description for the remote, e.g. for display
               in a UI. The description is stored in the repository summary.

           --homepage=URL
               URL for a website for the remote, e.g. for display in a UI.
               The url is stored in the repository summary.

           --icon=URL
               URL for an icon for the remote, e.g. for display in a UI. The
               url is stored in the repository summary.

           --default-branch=BRANCH
               A default branch for the repository, mainly for use in a UI.

           --gpg-import=FILE
               Import a new default GPG public key from the given file.

           --collection-id=COLLECTION-ID
               The globally unique identifier of the remote repository, to
               allow mirrors to be grouped. This must be set to a globally
               unique reverse DNS string if the repository is to be made
               publicly available. If a collection ID is already set on an
               existing repository, this will update it. If not specified,
               the existing collection ID will be left unchanged.

           --deploy-collection-id
               Deploy the collection ID (set using --collection-id) in the
               static remote configuration for all clients. This is
               irrevocable once published in a repository. Use it to decide
               when to roll out a collection ID to users of an existing
               repository. If constructing a new repository which has a
               collection ID, you should typically always pass this option.

           --deploy-sideload-collection-id
               This is similar to --deploy-collection-id, but it only applies
               the deploy to clients newer than flatpak 1.7 which supports
               the new form of sideloads.

           --gpg-sign=KEYID
               Sign the commit with this GPG key. This option can be used
               multiple times.

           --gpg-homedir=PATH
               GPG Homedir to use when looking for keyrings

           --generate-static-deltas
               Generate static deltas for all references. This generates
               from-empty and delta static files that allow for faster
               download.

           --static-delta-jobs=NUM-JOBS
               Limit the number of parallel jobs creating static deltas. The
               default is the number of cpus.

           --static-delta-ignore-ref=PATTERN
               Don't generate deltas for runtime or application id matching
               this pattern. For instance,
               --static-delta-ignore-ref=*.Sources means there will not be
               any deltas for source refs.

           --prune
               Remove unreferenced objects in repo.

           --prune-depth
               Only keep at most this number of old versions for any
               particular ref. Default is -1 which means infinite.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#SEE_ALSO)SEE ALSO

           ostree(1), flatpak(1), flatpak-remote-ls(1),
           flatpak-build-export(1)

## [](#COLOPHON)COLOPHON

           This page is part of the flatpak (a tool for building and
           distributing desktop applications on Linux) project.  Information
           about the project can be found at ⟨http://flatpak.org/⟩.  It is
           not known how to report bugs for this man page; if you know,
           please send a mail to man-pages@man7.org.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/flatpak/flatpak⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    flatpak                                            FLATPAK BUILD-UPDAT(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-build-bundle(1)](../man1/flatpak-build-bundle.1.html),  [flatpak-build-commit-from(1)](../man1/flatpak-build-commit-from.1.html),  [flatpak-build-export(1)](../man1/flatpak-build-export.1.html),  [flatpak-build-import-bundle(1)](../man1/flatpak-build-import-bundle.1.html),  [flatpak-repo(1)](../man1/flatpak-repo.1.html)

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
