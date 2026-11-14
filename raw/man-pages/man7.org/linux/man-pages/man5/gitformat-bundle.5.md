---
{"title": "gitformat-bundle(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/gitformat-bundle.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gitformat-bundle(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [FORMAT](#FORMAT) \| [SEMANTICS](#SEMANTICS) \| [CAPABILITIES](#CAPABILITIES) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GITFORMAT-BUNDLE(5)             Git Manual            GITFORMAT-BUNDLE(5)

## [](#NAME)NAME

           gitformat-bundle - The bundle file format

## [](#SYNOPSIS)SYNOPSIS

           *.bundle
           *.bdl

## [](#DESCRIPTION)DESCRIPTION

           The Git bundle format is a format that represents both refs and
           Git objects. A bundle is a header in a format similar to
           git-show-ref(1) followed by a pack in *.pack format.

           The format is created and read by the git-bundle(1) command, and
           supported by e.g. git-fetch(1) and git-clone(1).

## [](#FORMAT)FORMAT

           We will use ABNF notation to define the Git bundle format. See
           gitprotocol-common(5) for the details.

           A v2 bundle looks like this:

               bundle    = signature *prerequisite *reference LF pack
               signature = "# v2 git bundle" LF

               prerequisite = "-" obj-id SP comment LF
               comment      = *CHAR
               reference    = obj-id SP refname LF

               pack         = ... ; packfile

           A v3 bundle looks like this:

               bundle    = signature *capability *prerequisite *reference LF pack
               signature = "# v3 git bundle" LF

               capability   = "@" key ["=" value] LF
               prerequisite = "-" obj-id SP comment LF
               comment      = *CHAR
               reference    = obj-id SP refname LF
               key          = 1*(ALPHA / DIGIT / "-")
               value        = *(%01-09 / %0b-FF)

               pack         = ... ; packfile

## [](#SEMANTICS)SEMANTICS

           A Git bundle consists of several parts.

           •   "Capabilities", which are only in the v3 format, indicate
               functionality that the bundle requires to be read properly.

           •   "Prerequisites" list the objects that are NOT included in the
               bundle and the reader of the bundle MUST already have, in
               order to use the data in the bundle. The objects stored in the
               bundle may refer to prerequisite objects and anything
               reachable from them (e.g. a tree object in the bundle can
               reference a blob that is reachable from a prerequisite) and/or
               expressed as a delta against prerequisite objects.

           •   "References" record the tips of the history graph, iow, what
               the reader of the bundle CAN "git fetch" from it.

           •   "Pack" is the pack data stream "git fetch" would send, if you
               fetch from a repository that has the references recorded in
               the "References" above into a repository that has references
               pointing at the objects listed in "Prerequisites" above.

           In the bundle format, there can be a comment following a
           prerequisite obj-id. This is a comment and it has no specific
           meaning. The writer of the bundle MAY put any string here. The
           reader of the bundle MUST ignore the comment.

       Note on shallow clones and Git bundles
           Note that the prerequisites do not represent a shallow-clone
           boundary. The semantics of the prerequisites and the shallow-clone
           boundaries are different, and the Git bundle v2 format cannot
           represent a shallow clone repository.

## [](#CAPABILITIES)CAPABILITIES

           Because there is no opportunity for negotiation, unknown
           capabilities cause git bundle to abort.

           •   object-format specifies the hash algorithm in use, and can
               take the same values as the extensions.objectFormat
               configuration value.

           •   filter specifies an object filter as in the --filter option in
               git-rev-list(1). The resulting pack-file must be marked as a
               .promisor pack-file after it is unbundled.

## [](#GIT)GIT

           Part of the git(1) suite

## [](#COLOPHON)COLOPHON

           This page is part of the git (Git distributed version control
           system) project.  Information about the project can be found at 
           ⟨http://git-scm.com/⟩.  If you have a bug report for this manual
           page, see ⟨http://git-scm.com/community⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/git/git.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Git 2.55.0.493.g5b2471          2026-08-03            GITFORMAT-BUNDLE(5)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-bundle(1)](../man1/git-bundle.1.html),  [gitformat-pack(5)](../man5/gitformat-pack.5.html)

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
