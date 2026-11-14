---
{"title": "git-column(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-column.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-column(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [CONFIGURATION](#CONFIGURATION) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-COLUMN(1)                   Git Manual                  GIT-COLUMN(1)

## [](#NAME)NAME

           git-column - Display data in columns

## [](#SYNOPSIS)SYNOPSIS

           git column [--command=<name>] [--[raw-]mode=<mode>] [--width=<width>]
                        [--indent=<string>] [--nl=<string>] [--padding=<n>]

## [](#DESCRIPTION)DESCRIPTION

           This command formats the lines of its standard input into a table
           with multiple columns. Each input line occupies one cell of the
           table. It is used internally by other git commands to format
           output into columns.

## [](#OPTIONS)OPTIONS

           --command=<name>
               Look up layout mode using configuration variable column.<name>
               and column.ui.

           --mode=<mode>
               Specify layout mode. See configuration variable column.ui for
               option syntax in git-config(1).

           --raw-mode=<n>
               Same as --mode but take mode encoded as a number. This is
               mainly used by other commands that have already parsed layout
               mode.

           --width=<width>
               Specify the terminal width. By default git column will detect
               the terminal width, or fall back to 80 if it is unable to do
               so.

           --indent=<string>
               String to be printed at the beginning of each line.

           --nl=<string>
               String to be printed at the end of each line, including
               newline character.

           --padding=<N>
               The number of spaces between columns. One space by default.

## [](#EXAMPLES)EXAMPLES

           Format data by columns:

               $ seq 1 24 | git column --mode=column --padding=5
               1      4      7      10     13     16     19     22
               2      5      8      11     14     17     20     23
               3      6      9      12     15     18     21     24

           Format data by rows:

               $ seq 1 21 | git column --mode=row --padding=5
               1      2      3      4      5      6      7
               8      9      10     11     12     13     14
               15     16     17     18     19     20     21

           List some tags in a table with unequal column widths:

               $ git tag --list 'v2.4.*' --column=row,dense
               v2.4.0  v2.4.0-rc0  v2.4.0-rc1  v2.4.0-rc2  v2.4.0-rc3
               v2.4.1  v2.4.10     v2.4.11     v2.4.12     v2.4.2
               v2.4.3  v2.4.4      v2.4.5      v2.4.6      v2.4.7
               v2.4.8  v2.4.9

## [](#CONFIGURATION)CONFIGURATION

           Everything below this line in this section is selectively included
           from the git-config(1) documentation. The content is the same as
           what’s found there:

           column.ui
               Specify whether supported commands should output in columns.
               This variable consists of a list of tokens separated by spaces
               or commas:

               These options control when the feature should be enabled
               (defaults to never):

               always
                   always show in columns

               never
                   never show in columns

               auto
                   show in columns if the output is to the terminal

               These options control layout (defaults to column). Setting any
               of these implies always if none of always, never, or auto are
               specified.

               column
                   fill columns before rows

               row
                   fill rows before columns

               plain
                   show in one column

               Finally, these options can be combined with a layout option
               (defaults to nodense):

               dense
                   make unequal size columns to utilize more space

               nodense
                   make equal size columns

           column.branch
               Specify whether to output branch listing in git branch in
               columns. See column.ui for details.

           column.clean
               Specify the layout when listing items in git clean -i, which
               always shows files and directories in columns. See column.ui
               for details.

           column.status
               Specify whether to output untracked files in git status in
               columns. See column.ui for details.

           column.tag
               Specify whether to output tag listings in git tag in columns.
               See column.ui for details.

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

    Git 2.55.0.493.g5b2471          2026-08-03                  GIT-COLUMN(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html)

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
