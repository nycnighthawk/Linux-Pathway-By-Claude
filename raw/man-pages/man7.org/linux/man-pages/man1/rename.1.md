---
{"title": "rename(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rename.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rename(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [WARNING](#WARNING) \| [EDGE CASES](#EDGE_CASES) \| [INTERACTIVE MODE](#INTERACTIVE_MODE) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RENAME(1)                     User Commands                     RENAME(1)

## [](#NAME)NAME

           rename - rename files

## [](#SYNOPSIS)SYNOPSIS

           rename [options] substring replacement file...

## [](#DESCRIPTION)DESCRIPTION

           rename will rename the specified files by replacing the first
           occurrence of substring in their name by replacement.

## [](#OPTIONS)OPTIONS

           -s, --symlink
               Do not rename a symbolic link but change where it points.

           -c, --copy
               Copy files instead of renaming them. The original files remain
               unchanged. For regular files, the content is copied and
               permission bits (S_IRWXU|S_IRWXG|S_IRWXO) are preserved, but
               ownership, timestamps, and extended attributes are not. For
               symbolic links, a new link with the same target is created.

           -v, --verbose
               Show which files were renamed, if any.

           -n, --no-act
               Do not make any changes; add --verbose to see what would be
               made.

           -a, --all
               Replace all occurrences of substring rather than only the
               first one.

           -l, --last
               Replace the last occurrence of substring rather than the first
               one.

           -o, --no-overwrite
               Do not overwrite existing files. When --symlink is active, do
               not overwrite symbolic links pointing to existing targets.

           -i, --interactive
               Ask before overwriting existing files.

           -h, --help
               Display help text and exit.

           -V, --version
               Display version and exit.

## [](#WARNING)WARNING

           The renaming has no safeguards by default or without any one of
           the options --no-overwrite, --interactive or --no-act. If the user
           has permission to rewrite filenames, the command will perform the
           action without any questions. For example, the result can be quite
           drastic when the command is run as root in the /lib directory.
           Always make a backup before running the command, unless you truly
           know what you are doing.

## [](#EDGE_CASES)EDGE CASES

           If substring is empty, then by default replacement will be added
           to the start of the filename. With --all, replacement will be
           inserted in between every two characters of the filename, as well
           as at the start and end.

           Normally, only the final path component of a filename is updated.
           (Or with --symlink, only the final path component of the link.)
           But if either substring or replacement contains a /, the full path
           is updated. This can cause a file to be moved between folders.
           Creating folders, and moving files between filesystems, is not
           supported.

## [](#INTERACTIVE_MODE)INTERACTIVE MODE

           As most standard utilities rename can be used with a terminal
           device (tty in short) in canonical mode, where the line is
           buffered by the tty and you press ENTER to validate the user
           input. If you put your tty in cbreak mode however, rename requires
           only a single key press to answer the prompt. To set cbreak mode,
           run for example:

               sh -c 'stty -icanon min 1; "$0" "$@"; stty icanon' rename -i from to files

## [](#EXIT_STATUS)EXIT STATUS

           0
               all requested rename operations were successful

           1
               all rename operations failed

           2
               some rename operations failed

           4
               nothing was renamed

           64
               unanticipated error occurred

## [](#EXAMPLES)EXAMPLES

           Given the files foo1, ..., foo9, foo10, ..., foo278, the commands

               rename foo foo00 foo?
               rename foo foo0 foo??

           will turn them into foo001, ..., foo009, foo010, ..., foo278. And

               rename .htm .html *.htm

           will fix the extension of your html files. Provide an empty string
           for shortening:

               rename '_with_long_name' '' file_with_long_name.*

           will remove the substring in the filenames.

## [](#SEE_ALSO)SEE ALSO

           mv(1)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The rename command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                      RENAME(1)

------------------------------------------------------------------------

Pages that refer to this page: [rename(2)](../man2/rename.2.html)

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
