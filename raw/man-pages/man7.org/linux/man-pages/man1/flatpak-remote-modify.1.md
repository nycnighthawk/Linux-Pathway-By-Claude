---
{"title": "flatpak-remote-modify(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-remote-modify.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-remote-modify(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK REMOTE-MODI(1)    flatpak remote-modify    FLATPAK REMOTE-MODI(1)

## [](#NAME)NAME

           flatpak-remote-modify - Modify a remote repository

## [](#SYNOPSIS)SYNOPSIS

           flatpak remote-modify [OPTION...] NAME

## [](#DESCRIPTION)DESCRIPTION

           Modifies options for an existing remote repository in the flatpak
           repository configuration.  NAME is the name for the remote.

           Unless overridden with the --system, --user, or --installation
           options, this command uses either the default system-wide
           installation or the per-user one, depending on which has the
           specified REMOTE.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --user
               Modify the per-user configuration.

           --system
               Modify the default system-wide configuration.

           --installation=NAME
               Modify a system-wide installation specified by NAME among
               those defined in /etc/flatpak/installations.d/. Using
               --installation=default is equivalent to using --system.

           --no-gpg-verify
               Disable GPG verification for the added remote.

           --gpg-verify
               Enable GPG verification for the added remote.

           --prio=PRIO
               Set the priority for the remote. Default is 1, higher is more
               prioritized. This is mainly used for graphical installation
               tools.

           --subset=SUBSET
               Limit the refs available from the remote to those that are
               part of the named subset.

           --no-enumerate
               Mark the remote as not enumerated. This means the remote will
               not be used to list applications, for instance in graphical
               installation tools. It will also not be used for runtime
               dependency resolution (as with --no-use-for-deps).

           --no-use-for-deps
               Mark the remote as not to be used for automatic runtime
               dependency resolution.

           --disable
               Disable the remote. Disabled remotes will not be automatically
               updated from.

           --enable
               Enable the remote.

           --enumerate
               Mark the remote as enumerated. This means the remote will be
               used to list applications, for instance in graphical
               installation tools.

           --use-for-deps
               Mark the remote as to be used for automatic runtime dependency
               resolution.

           --title=TITLE
               A title for the remote, e.g. for display in a UI.

           --comment=COMMENT
               A single-line comment for the remote, e.g. for display in a
               UI.

           --description=DESCRIPTION
               A full-paragraph description for the remote, e.g. for display
               in a UI.

           --homepage=URL
               URL for a website for the remote, e.g. for display in a UI.

           --icon=URL
               URL for an icon for the remote, e.g. for display in a UI.

           --default-branch=BRANCH
               A default branch for the remote, mainly for use in a UI.

           --collection-id=COLLECTION-ID
               The globally unique identifier of the remote repository, to
               allow mirrors to be grouped. This must only be set to the
               collection ID provided by the remote, and must not be set if
               the remote does not provide a collection ID.

           --url=URL
               Set a new URL.

           --update-metadata
               Update the remote's extra metadata from the OSTree
               repository's summary file. Only xa.title and xa.default-branch
               are supported at the moment.

           --no-filter, --filter=FILE
               Modify the path (or unset) for the local filter used for this
               remote. See flatpak-remote-add(1) for details about the filter
               file format.

           --gpg-import=FILE
               Import gpg keys from the specified keyring file as trusted for
               the new remote. If the file is - the keyring is read from
               standard input.

           --signature-lookaside=URL
               Specify an URL to be used to look up signatures for this
               remote (OCI remotes only).

           --authenticator-name=NAME
               Specify the authenticator to use for the remote.

           --authenticator-option=KEY=VALUE
               Specify an authenticator option for the remote.

           --authenticator-install
               Enable auto-installation of authenticator.

           --no-authenticator-install
               Disable auto-installation of authenticator.

           --follow-redirect
               Follow xa.redirect-url defined in the summary file.

           --no-follow-redirect
               Do not follow xa.redirect-url defined in the summary file.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak --user remote-modify --no-gpg-verify test-repo

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-remote-add(1), flatpak-remote-delete(1),
           flatpak-remotes(1)

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

    flatpak                                            FLATPAK REMOTE-MODI(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-config(1)](../man1/flatpak-config.1.html),  [flatpak-remote-add(1)](../man1/flatpak-remote-add.1.html),  [flatpak-remote-delete(1)](../man1/flatpak-remote-delete.1.html),  [flatpak-remote(5)](../man5/flatpak-remote.5.html)

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
