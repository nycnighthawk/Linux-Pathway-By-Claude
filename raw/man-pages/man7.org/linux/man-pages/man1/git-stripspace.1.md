---
{"title": "git-stripspace(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-stripspace.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-stripspace(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-STRIPSPACE(1)               Git Manual              GIT-STRIPSPACE(1)

## [](#NAME)NAME

           git-stripspace - Remove unnecessary whitespace

## [](#SYNOPSIS)SYNOPSIS

           git stripspace [-s | --strip-comments]
           git stripspace [-c | --comment-lines]

## [](#DESCRIPTION)DESCRIPTION

           Read text, such as commit messages, notes, tags and branch
           descriptions, from the standard input and clean it in the manner
           used by Git.

           With no arguments, this will:

           •   remove trailing whitespace from all lines

           •   collapse multiple consecutive empty lines into one empty line

           •   remove empty lines from the beginning and end of the input

           •   add a missing \n to the last line if necessary.

           In the case where the input consists entirely of whitespace
           characters, no output will be produced.

           NOTE: This is intended for cleaning metadata. Prefer the
           --whitespace=fix mode of git-apply(1) for correcting whitespace of
           patches or files in the repository.

## [](#OPTIONS)OPTIONS

           -s, --strip-comments
               Skip and remove all lines starting with a comment character
               (core.commentChar, default #).

           -c, --comment-lines
               Prepend the comment character and a blank space to each line.
               Lines will automatically be terminated with a newline. On
               empty lines, only the comment character will be prepended.

## [](#EXAMPLES)EXAMPLES

           Given the following noisy input with $ indicating the end of a
           line:

               |A brief introduction   $
               |   $
               |$
               |A new paragraph$
               |# with a commented-out line    $
               |explaining lots of stuff.$
               |$
               |# An old paragraph, also commented-out. $
               |      $
               |The end.$
               |  $

           Use git stripspace with no arguments to obtain:

               |A brief introduction$
               |$
               |A new paragraph$
               |# with a commented-out line$
               |explaining lots of stuff.$
               |$
               |# An old paragraph, also commented-out.$
               |$
               |The end.$

           Use git stripspace --strip-comments to obtain:

               |A brief introduction$
               |$
               |A new paragraph$
               |explaining lots of stuff.$
               |$
               |The end.$

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

    Git 2.55.0.493.g5b2471          2026-08-03              GIT-STRIPSPACE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-notes(1)](../man1/git-notes.1.html)

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
