---
{"title": "git-symbolic-ref(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-symbolic-ref.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-symbolic-ref(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                  |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-SYMBOLIC-REF(1)             Git Manual            GIT-SYMBOLIC-REF(1)

## [](#NAME)NAME

           git-symbolic-ref - Read, modify and delete symbolic refs

## [](#SYNOPSIS)SYNOPSIS

           git symbolic-ref [-m <reason>] <name> <ref>
           git symbolic-ref [-q] [--short] [--no-recurse] <name>
           git symbolic-ref --delete [-q] <name>

## [](#DESCRIPTION)DESCRIPTION

           Given one argument, reads which branch head the given symbolic ref
           refers to and outputs its path, relative to the .git/ directory.
           Typically you would give HEAD as the <name> argument to see which
           branch your working tree is on.

           Given two arguments, creates or updates a symbolic ref <name> to
           point at the given branch <ref>.

           Given --delete and an additional argument, deletes the given
           symbolic ref.

           A symbolic ref is a regular file that stores a string that begins
           with ref: refs/. For example, your .git/HEAD is a regular file
           whose content is ref: refs/heads/master.

## [](#OPTIONS)OPTIONS

           -d, --delete
               Delete the symbolic ref <name>.

           -q, --quiet
               Do not issue an error message if the <name> is not a symbolic
               ref but a detached HEAD; instead exit with non-zero status
               silently.

           --short
               When showing the value of <name> as a symbolic ref, try to
               shorten the value, e.g. from refs/heads/master to master.

           --recurse, --no-recurse
               When showing the value of <name> as a symbolic ref, if <name>
               refers to another symbolic ref, follow such a chain of
               symbolic refs until the result no longer points at a symbolic
               ref (--recurse, which is the default).  --no-recurse stops
               after dereferencing only a single level of symbolic ref.

           -m
               Update the reflog for <name> with <reason>. This is valid only
               when creating or updating a symbolic ref.

## [](#NOTES)NOTES

           In the past, .git/HEAD was a symbolic link pointing at
           refs/heads/master. When we wanted to switch to another branch, we
           did ln -sf refs/heads/newbranch .git/HEAD, and when we wanted to
           find out which branch we are on, we did readlink .git/HEAD. But
           symbolic links are not entirely portable, so they are now
           deprecated and symbolic refs (as described above) are used by
           default.

           git symbolic-ref will exit with status 0 if the contents of the
           symbolic ref were printed correctly, with status 1 if the
           requested name is not a symbolic ref, or 128 if another error
           occurs.

## [](#SEE_ALSO)SEE ALSO

           git-update-ref(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03            GIT-SYMBOLIC-REF(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-update-ref(1)](../man1/git-update-ref.1.html),  [gitglossary(7)](../man7/gitglossary.7.html)

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
