---
{"title": "git-mailsplit(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-mailsplit.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-mailsplit(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-MAILSPLIT(1)                Git Manual               GIT-MAILSPLIT(1)

## [](#NAME)NAME

           git-mailsplit - Simple UNIX mbox splitter program

## [](#SYNOPSIS)SYNOPSIS

           git mailsplit [-b] [-f<nn>] [-d<prec>] [--keep-cr] [--mboxrd]
                           -o<directory> [--] [(<mbox>|<Maildir>)...]

## [](#DESCRIPTION)DESCRIPTION

           Splits a mbox file or a Maildir into a list of files: "0001"
           "0002" .. in the specified directory so you can process them
           further from there.

               Important

               Maildir splitting relies upon filenames being sorted to output
               patches in the correct order.

## [](#OPTIONS)OPTIONS

           <mbox>
               Mbox file to split. If not given, the mbox is read from the
               standard input.

           <Maildir>
               Root of the Maildir to split. This directory should contain
               the cur, tmp and new subdirectories.

           -o<directory>
               Directory in which to place the individual messages.

           -b
               If any file doesn’t begin with a From line, assume it is a
               single mail message instead of signaling an error.

           -d<prec>
               Instead of the default 4 digits with leading zeros, different
               precision can be specified for the generated filenames.

           -f<nn>
               Skip the first <nn> numbers, for example if -f3 is specified,
               start the numbering with 0004.

           --keep-cr
               Do not remove \r from lines ending with \r\n.

           --mboxrd
               Input is of the "mboxrd" format and "^>+From " line escaping
               is reversed.

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

    Git 2.55.0.493.g5b2471          2026-08-03               GIT-MAILSPLIT(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-am(1)](../man1/git-am.1.html),  [git-config(1)](../man1/git-config.1.html)

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
