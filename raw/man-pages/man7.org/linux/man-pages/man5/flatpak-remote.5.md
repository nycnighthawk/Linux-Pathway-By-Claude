---
{"title": "flatpak-remote(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/flatpak-remote.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-remote(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK REMOTE(5)             flatpak remote            FLATPAK REMOTE(5)

## [](#NAME)NAME

           flatpak-remote - Configuration for a remote

## [](#DESCRIPTION)DESCRIPTION

           Flatpak stores information about configured remotes for an
           installation location in $installation/repo/config. For example,
           the remotes for the default system-wide installation are in
           $prefix/var/lib/flatpak/repo/config, and the remotes for the
           per-user installation are in
           $HOME/.local/share/flatpak/repo/config.

           Normally, it is not necessary to edit remote config files
           directly, the flatpak remote-modify command should be used to
           change properties of remotes.

           System-wide remotes can be statically preconfigured by dropping
           flatpakrepo(5) files into /usr/share/flatpak/remotes.d/ and
           /etc/flatpak/remotes.d/. Ifa file with the same name exists in
           both, the file under /etc will take precedence.

## [](#FILE_FORMAT)FILE FORMAT

           The remote config file format is using the same .ini file format
           that is used for systemd unit files or application .desktop files.

       [remote ...]
           All the configuration for the the remote with name NAME is
           contained in the [remote "NAME"] group.

           The following keys are recognized by OSTree, among others:

           url (string)
               The url for the remote. An URL of the form oci+https:// or
               oci+http:// is a Flatpak extension that indicates that the
               remote is not an ostree repository, but is rather an URL to an
               index of OCI images that are stored within a container image
               registry.

               For OCI remotes, client and CA certificates are read from
               /etc/containers/certs.d and ~/.config/containers/certs.d as
               documented in containers-certs.d(5).

           gpg-verify (boolean)
               Whether to use GPG verification for content from this remote.

           gpg-verify-summary (boolean)
               Whether to use GPG verification for the summary of this
               remote.

               This is ignored if collection-id is set, as refs are verified
               in commit metadata in that case. Enabling gpg-verify-summary
               would break peer to peer distribution of refs.

           collection-id (string)
               The globally unique identifier for the upstream collection
               repository, to allow mirrors to be grouped.

           All flatpak-specific keys have a xa. prefix:

           xa.disable (boolean)
               Whether the remote is disabled. Defaults to false.

           xa.prio (integer)
               The priority for the remote. This is used when listing
               remotes, and when searching them for the runtime needed by an
               app. The remote providing the app is searched for its runtime
               before others with equal priority. Defaults to 1.

           xa.noenumerate (boolean)
               Whether this remote should be ignored when presenting
               available apps/runtimes, or when searching for a runtime
               dependency. Defaults to false.

           xa.nodeps (boolean)
               Whether this remote should be excluded when searching for
               dependencies. Defaults to false.

           xa.title (string)
               An optional title to use when presenting this remote in a UI.

           xa.title-is-set (boolean)
               This key is set to true if xa.title has been explicitly set.

           xa.comment (string)
               An optional single-line comment to use when presenting this
               remote in a UI.

           xa.comment-is-set (boolean)
               This key is set to true if xa.comment has been explicitly set.

           xa.description (string)
               An optional full-paragraph of text to use when presenting this
               remote in a UI.

           xa.description-is-set (boolean)
               This key is set to true if xa.description has been explicitly
               set.

           xa.homepage (string)
               An optional URL that points to a website for this repository
               to use when presenting this remote in a UI.

           xa.homepage-is-set (boolean)
               This key is set to true if xa.homepage has been explicitly
               set.

           xa.icon (string)
               An optional URL that points to an icon for this repository to
               use when presenting this remote in a UI.

           xa.icon-is-set (boolean)
               This key is set to true if xa.icon has been explicitly set.

           xa.default-branch (string)
               The default branch to use when installing from this remote.

           xa.default-branch-is-set (boolean)
               This key is set to true if xa.default-branch has been
               explicitly set.

           xa.main-ref (string)
               The main reference served by this remote. This is used for
               origin remotes of applications installed via a flatpakref
               file.

           xa.signature-lookaside (string)
               URL to load signatures from (OCI remotes only), using the
               containers/image separate storage mechanism.[1]

## [](#EXAMPLES)EXAMPLES

               [remote "gnome-nightly-apps"]
               gpg-verify=true
               gpg-verify-summary=true
               url=https://sdk.gnome.org/nightly/repo-apps/
               xa.title=GNOME Applications

               [remote "flathub"]
               gpg-verify=true
               gpg-verify-summary=false
               collection-id=org.flathub.Stable
               url=https://dl.flathub.org/repo/
               xa.title=Flathub

## [](#SEE_ALSO)SEE ALSO

           flatpak-remote-modify(1)

## [](#NOTES)NOTES

            1. containers/image separate storage mechanism.
               https://github.com/containers/image/blob/main/docs/signature-protocols.md

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

    flatpak                                                 FLATPAK REMOTE(5)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html)

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
