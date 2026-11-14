---
{"title": "git-check-mailmap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-check-mailmap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-check-mailmap(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [CONFIGURATION](#CONFIGURATION) \| [MAPPING AUTHORS](#MAPPING_AUTHORS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-CHECK-MAILMAP(1)            Git Manual           GIT-CHECK-MAILMAP(1)

## [](#NAME)NAME

           git-check-mailmap - Show canonical names and email addresses of
           contacts

## [](#SYNOPSIS)SYNOPSIS

           git check-mailmap [<options>] <contact>...

## [](#DESCRIPTION)DESCRIPTION

           For each “Name <user@host>”, “<user@host>”, or “user@host” from
           the command-line or standard input (when using --stdin), look up
           the person’s canonical name and email address (see "Mapping
           Authors" below). If found, print them; otherwise print the input
           as-is.

## [](#OPTIONS)OPTIONS

           --stdin
               Read contacts, one per line, from the standard input after
               exhausting contacts provided on the command-line.

           --mailmap-file=<file>
               In addition to any configured mailmap files, read the
               specified mailmap file. Entries in this file take precedence
               over entries in either the default mailmap file or any
               configured mailmap file.

           --mailmap-blob=<blob>
               Like --mailmap-file, but consider the value as a reference to
               a blob in the repository. If both --mailmap-file and
               --mailmap-blob are specified, entries in --mailmap-file will
               take precedence.

## [](#OUTPUT)OUTPUT

           For each contact, a single line is output, terminated by a
           newline. If the name is provided or known to the mailmap, “Name
           <user@host>” is printed; otherwise only “<user@host>” is printed.

## [](#CONFIGURATION)CONFIGURATION

           See mailmap.file and mailmap.blob in git-config(1) for how to
           specify a custom .mailmap target file or object.

## [](#MAPPING_AUTHORS)MAPPING AUTHORS

           See gitmailmap(5).

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

    Git 2.55.0.493.g5b2471          2026-08-03           GIT-CHECK-MAILMAP(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [gitmailmap(5)](../man5/gitmailmap.5.html)

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
