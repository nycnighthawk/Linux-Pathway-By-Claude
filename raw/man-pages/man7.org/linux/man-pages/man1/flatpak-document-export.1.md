---
{"title": "flatpak-document-export(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-document-export.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-document-export(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK DOCUMENT-EX(1)   flatpak document-export   FLATPAK DOCUMENT-EX(1)

## [](#NAME)NAME

           flatpak-document-export - Export a file to a sandboxed application

## [](#SYNOPSIS)SYNOPSIS

           flatpak document-export [OPTION...] FILE

## [](#DESCRIPTION)DESCRIPTION

           Creates a document id for a local file that can be exposed to
           sandboxed applications, allowing them access to files that they
           would not otherwise see. The exported files are exposed in a fuse
           filesystem at /run/user/$UID/doc/.

           This command also lets you modify the per-application permissions
           of the documents, granting or revoking access to the file on a
           per-application basis.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           -u, --unique
               Don't reuse an existing document id for the file. This makes
               it safe to later remove the document when you're finished with
               it.

           -t, --transient
               The document will only exist for the length of the session.
               This is useful for temporary grants.

           -n, --noexist
               Don't require the file to exist already.

           -a, --app=APPID
               Grant read access to the specified application. The --allow
               and --forbid options can be used to grant or remove additional
               privileges. This option can be used multiple times.

           -r, --allow-read
               Grant read access to the applications specified with --app.
               This defaults to TRUE.

           --forbid-read
               Revoke read access for the applications specified with --app.

           -w, --allow-write
               Grant write access to the applications specified with --app.

           --forbid-write
               Revoke write access for the applications specified with --app.

           -d, --allow-delete
               Grant the ability to remove the document from the document
               portal to the applications specified with --app.

           --forbid-delete
               Revoke the ability to remove the document from the document
               portal from the applications specified with --app.

           -g, --allow-grant-permission
               Grant the ability to grant further permissions to the
               applications specified with --app.

           --forbid-grant-permission
               Revoke the ability to grant further permissions for the
               applications specified with --app.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           $ flatpak document-export --app=org.gnome.gedit ~/test.txt

               /run/user/1000/doc/e52f9c6a/test.txt

## [](#SEE_ALSO)SEE ALSO

           flatpak(1), flatpak-document-unexport(1),
           flatpak-document-info(1), flatpak-documents(1)

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

    flatpak                                            FLATPAK DOCUMENT-EX(1)

------------------------------------------------------------------------

Pages that refer to this page: [flatpak(1)](../man1/flatpak.1.html),  [flatpak-document-info(1)](../man1/flatpak-document-info.1.html),  [flatpak-documents(1)](../man1/flatpak-documents.1.html),  [flatpak-document-unexport(1)](../man1/flatpak-document-unexport.1.html)

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
