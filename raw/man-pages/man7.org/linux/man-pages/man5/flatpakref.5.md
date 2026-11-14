---
{"title": "flatpakref(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/flatpakref.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpakref(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILE FORMAT](#FILE_FORMAT) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                      |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAKREF(5)                   flatpakref                  FLATPAKREF(5)

## [](#NAME)NAME

           flatpakref - Reference to a remote for an application or runtime

## [](#DESCRIPTION)DESCRIPTION

           Flatpak uses flatpakref files to share information about a remote
           for a single application. The flatpakref file contains enough
           information to add the remote and install the application. Use the
           flatpak install --from command to do so.

           flatpakref files may also contain additional information that is
           useful when displaying the application to the user, e.g. in an app
           store.

           The filename extension commonly used for flatpakref files is
           .flatpakref.

           A flatpakref file can also refer to a remote for a runtime.

## [](#FILE_FORMAT)FILE FORMAT

           The flatpakref file is using the same .ini file format that is
           used for systemd unit files or application .desktop files.

       [Flatpak Ref]
           All the information is contained in the [Flatpak Ref] group.

           The following keys can be present in this group:

           Version (uint64)
               The version of the file format, must be 1 if present.

           Name (string)
               The fully qualified name of the runtime or application. This
               key is mandatory.

           Url (string)
               The url for the remote. This key is mandatory.

           Branch (string)
               The name of the branch from which to install the application
               or runtime. If this key is not specified, the "master" branch
               is used.

           Title (string)
               The title of the application or runtime. This should be a
               user-friendly name that can be displayed e.g. in an app store.

           Comment (string)
               A short summary of the application or runtime, for display
               e.g. in an app store.

           Description (string)
               A longer description of the application or runtime, for
               display e.g. in an app store.

           Icon (string)
               The url for an icon that can be used to represent the
               application or runtime.

           Homepage (string)
               The url of a webpage describing the application or runtime.

           DeploySideloadCollectionID (string)
               The collection ID of the remote, if it has one. This uniquely
               identifies the collection of apps in the remote, to allow peer
               to peer redistribution (see flatpak(1)). It is recommended to
               use this key over DeployCollectionID or CollectionID because
               only newer clients (Flatpak 1.12.8 or later) pay attention to
               it (and older clients don't handle collection IDs properly).

           DeployCollectionID (string)
               This is deprecated but still supported for backwards
               compatibility. Use DeploySideloadCollectionID instead.

           CollectionID (string)
               This is deprecated but still supported for backwards
               compatibility. Use DeploySideloadCollectionID instead.

           IsRuntime (boolean)
               Whether this file refers to a runtime. If this key is not
               specified, the file is assumed to refer to an application.

           GPGKey (string)
               The base64-encoded gpg key for the remote.

           SignatureLookaside (string)
               URL to use to look up signatures (OCI remotes only)

           RuntimeRepo (string)
               The url for a .flatpakrepo file for the remote where the
               runtime can be found. Note that if the runtime is available in
               the remote providing the app, that remote may be used instead
               but the one specified by this option will still be added.

           SuggestRemoteName (string)
               A suggested name for the remote.

## [](#EXAMPLE)EXAMPLE

               [Flatpak Ref]
               Title=gedit
               Name=org.gnome.gedit
               Branch=stable
               Url=http://sdk.gnome.org/repo-apps/
               IsRuntime=false
               GPGKey=mQENBFUUCGcBCAC/K9WeV4xCaKr3NKRqPXeY5mpaXAJyasLqCtrDx92WUgbu0voWrhohNAKpqizod2dvzc/XTxm3rHyIxmNfdhz1gaGhynU75Qw4aJVcly2eghTIl++gfDtOvrOZo/VuAq30f32dMIgHQdRwEpgCwz7WyjpqZYltPAEcCNL4MTChAfiHJeeiQ5ibystNBW8W6Ymf7sO4m4g5+/aOxI54oCOzD9TwBAe+yXcJJWtc2rAhMCjtyPJzxd0ZVXqIzCe1xRvJ6Rq7YCiMbiM2DQFWXKnmYQbj4TGNMnwNdAajCdrcBWEMSbzq7EzuThIJRd8Ky4BkEe1St6tuqwFaMZz+F9eXABEBAAG0KEdub21lIFNESyAzLjE2IDxnbm9tZS1vcy1saXN0QGdub21lLm9yZz6JATgEEwECACIFAlUUCGcCGwMGCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEArkz6VV0VKBa5cH/0vXa31YgEjNk78gGFXqnQxdD1WYA87OYxDi189l4lA802EFTF4wCBuZyDOqdd5BhS3Ab0cR778DmZXRUP2gwe+1zTJypU2JMnDpkwJ4NK1VP6/tE4SAPrznBtmb76BKaWBqUfZ9Wq1zg3ugvqkZB/Exq+usypIOwQVp1KL58TrjBRda0HvRctzkNhr0qYAtkfLFe0GvksBp4vBm8uGwAx7fw/HbhIjQ9pekTwvB+5GwDPO/tSip/1bQfCS+XJB8Ffa04HYPLGedalnWBrwhYY+G/kn5Zh9L/AC8xeLwTJTHM212rBjPa9CWs9C6a57MSaeGIEHLC1hEyiJJ15w8jmY=
               DeployCollectionID=org.gnome.Apps

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-install(1) flatpakrepo(5),

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

    flatpak                                                     FLATPAKREF(5)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-install(1)](../man1/flatpak-install.1.html),  [flatpakrepo(5)](../man5/flatpakrepo.5.html)

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
