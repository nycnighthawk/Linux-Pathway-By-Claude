---
{"title": "flatpak-build-commit-from(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/flatpak-build-commit-from.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# flatpak-build-commit-from(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FLATPAK BUILD-COMMI(1)  flatpak build-commit-from  FLATPAK BUILD-COMMI(1)

## [](#NAME)NAME

           flatpak-build-commit-from - Create new commits based on existing
           one (possibly from another repository)

## [](#SYNOPSIS)SYNOPSIS

           flatpak build-commit-from [OPTION...] DST-REPO DST-REF...

## [](#DESCRIPTION)DESCRIPTION

           Creates new commits on the DST-REF branch in the DST-REPO, with
           the contents (and most of the metadata) taken from another branch,
           either from another repo, or from another branch in the same
           repository.

           The collection ID set on DST-REPO (if set) will be used for the
           newly created commits.

           This command is very useful when you want to maintain a branch
           with a clean history that has no unsigned or broken commits. For
           instance, you can import the head from a different repository from
           an automatic builder when you've verified that it worked. The new
           commit will have no parents or signatures from the autobuilder,
           and can be properly signed with the official key.

           Any deltas that affect the original commit and that match parent
           commits in the destination repository are copied and rewritten for
           the new commit id.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Show help options and exit.

           --src-repo=SRC-REPO
               The (local) repository to pull the source branch from.
               Defaults to the destination repository.

           --src-ref=SRC-REF
               The branch to use as the source for the new commit. Defaults
               to the same as the destination ref, which is useful only if a
               different source repo has been specified.

           --extra-collection-id=COLLECTION-ID
               Add an extra collection-ref binding for this collection, in
               addition to whatever would normally be added due to the
               destination repository collection id. This option can be used
               multiple times.

           --subset=SUBSET
               Mark the commit to be included in the named subset. This will
               cause the commit to be put in the named subset summary (in
               addition to the main one), allowing users to see only this
               subset instead of the whole repo.

           --untrusted
               The source repository is not trusted, all objects are copied
               (not hardlinked) and all checksums are verified.

           -s, --subject=SUBJECT
               One line subject for the commit message. If not specified,
               will be taken from the source commit.

           -b, --body=BODY
               Full description for the commit message. If not specified,
               will be taken from the source commit.

           --update-appstream
               Update the appstream branch after the build.

           --no-update-summary
               Don't update the summary file after the new commit is added.
               This means the repository will not be useful for serving over
               http until build-update-repo has been run. This is useful is
               you want to do multiple repo operations before finally
               updating the summary.

           --force
               Create new commit even if the content didn't change from the
               existing branch head.

           --disable-fsync
               Don't fsync when writing to the repository. This can result in
               data loss in exceptional situations, but can improve
               performance when working with temporary or test repositories.

           --gpg-sign=KEYID
               Sign the commit with this GPG key. This option can be used
               multiple times.

           --gpg-homedir=PATH
               GPG Homedir to use when looking for keyrings

           --end-of-life=REASON
               Mark build as end-of-life

           --end-of-life-rebase=OLDID=NEWID
               Mark new refs as end-of-life. Unlike --end-of-life, this one
               takes an ID that supersedes the current one. By the user's
               request, the application data may be preserved for the new
               application. Note, this is actually a prefix match, so if you
               say org.the.app=org.new.app, then something like
               org.the.app.Locale will be rebased to org.new.app.Locale.

           --timestamp=TIMESTAMP
               Override the timestamp of the commit. Use an ISO 8601
               formatted date, or NOW for the current time

           --disable-fsync
               Don't fsync when writing to the repository. This can result in
               data loss in exceptional situations, but can improve
               performance when working with temporary or test repositories.

           -v, --verbose
               Print debug information during command processing.

           --ostree-verbose
               Print OSTree debug information during command processing.

## [](#EXAMPLES)EXAMPLES

           To revert a commit to the commit before:

           $ flatpak build-commit-from --timestamp=NOW
           --src-ref=app/org.gnome.gedit/x86_64/master^ repo
           app/org.gnome.gedit/x86_64/master

## [](#SEE_ALSO)SEE ALSO

           ostree(1), flatpak(1), flatpak-build-init(1), flatpak-build(1),
           flatpak-build-finish(1), flatpak-build-sign(1),
           flatpak-build-update-repo(1)

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

    flatpak                                            FLATPAK BUILD-COMMI(1)

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
