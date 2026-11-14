---
{"title": "rm(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/rm.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# rm(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                     |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RM(1)                         User Commands                         RM(1)

## [](#NAME)NAME

           rm - remove files or directories

## [](#SYNOPSIS)SYNOPSIS

           rm [OPTION]... [FILE]...

## [](#DESCRIPTION)DESCRIPTION

           This manual page documents the GNU version of rm.  rm removes each
           specified file.  By default, it does not remove directories.

           If the -I or --interactive=once option is given, and there are
           more than three files or the -r, -R, or --recursive are given,
           then rm prompts the user for whether to proceed with the entire
           operation.  If the response is not affirmative, the entire command
           is aborted.

           Otherwise, if a file is unwritable, standard input is a terminal,
           and the -f or --force option is not given, or the -i or
           --interactive=always option is given, rm prompts the user for
           whether to remove the file.  If the response is not affirmative,
           the file is skipped.

## [](#OPTIONS)OPTIONS

           Remove (unlink) the FILE(s).

           -f, --force
                  ignore nonexistent files and arguments, never prompt

           -i     prompt before every removal

           -I     prompt once before removing more than three files, or when
                  removing recursively; less intrusive than -i, while still
                  giving protection against most mistakes

           --interactive[=WHEN]
                  prompt according to WHEN: never, once (-I), or always (-i);
                  without WHEN, prompt always

           --one-file-system
                  when removing a hierarchy recursively, skip any directory
                  that is on a file system different from that of the
                  corresponding command line argument

           --no-preserve-root
                  do not treat '/' specially

           --preserve-root[=all]
                  do not remove '/' (default); with 'all', reject any command
                  line argument on a separate device from its parent

           -r, -R, --recursive
                  remove directories and their contents recursively

           -d, --dir
                  remove empty directories

           -v, --verbose
                  explain what is being done

           --help display this help and exit

           --version
                  output version information and exit

           By default, rm does not remove directories.  Use the --recursive
           (-r or -R) option to remove each listed directory, too, along with
           all of its contents.

           Any attempt to remove a file whose last file name component is '.'
           or '..'  is rejected with a diagnostic.

           To remove a file whose name starts with a '-', for example '-foo',
           use one of these commands:

                  rm -- -foo

                  rm ./-foo

           If you use rm to remove a file, it might be possible to recover
           some of its contents, given sufficient expertise and/or time.  For
           greater assurance that the contents are unrecoverable, consider
           using shred(1).

## [](#AUTHOR)AUTHOR

           Written by Paul Rubin, David MacKenzie, Richard M. Stallman, and
           Jim Meyering.

## [](#REPORTING_BUGS)REPORTING BUGS

           Report bugs to: bug-coreutils@gnu.org
           GNU coreutils home page: <https://www.gnu.org/software/coreutils/>
           General help using GNU software: <https://www.gnu.org/gethelp/>
           Report any translation bugs to
           <https://translationproject.org/team/>

## [](#COPYRIGHT)COPYRIGHT

           Copyright © 2026 Free Software Foundation, Inc.  License GPLv3+:
           GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
           This is free software: you are free to change and redistribute it.
           There is NO WARRANTY, to the extent permitted by law.

## [](#SEE_ALSO)SEE ALSO

           unlink(1), unlink(2), chattr(1), shred(1)

           Full documentation <https://www.gnu.org/software/coreutils/rm>
           or available locally via: info '(coreutils) rm invocation'

## [](#COLOPHON)COLOPHON

           This page is part of the coreutils (basic file, shell and text
           manipulation utilities) project.  Information about the project
           can be found at ⟨http://www.gnu.org/software/coreutils/⟩.  If you
           have a bug report for this manual page, see
           ⟨http://www.gnu.org/software/coreutils/⟩.  This page was obtained
           from the tarball coreutils-9.11.tar.xz fetched from
           ⟨http://ftp.gnu.org/gnu/coreutils/⟩ on 2026-08-03.  If you
           discover any rendering problems in this HTML version of the page,
           or you believe there is a better or more up-to-date source for the
           page, or you have corrections or improvements to the information
           in this COLOPHON (which is not part of the original manual page),
           send a mail to man-pages@man7.org

    GNU coreutils 9.11              April 2026                          RM(1)

------------------------------------------------------------------------

Pages that refer to this page: [pmlock(1)](../man1/pmlock.1.html),  [rmdir(2)](../man2/rmdir.2.html),  [unlink(2)](../man2/unlink.2.html),  [remove(3)](../man3/remove.3.html),  [mq_overview(7)](../man7/mq_overview.7.html),  [symlink(7)](../man7/symlink.7.html),  [debugfs(8)](../man8/debugfs.8.html),  [lsof(8)](../man8/lsof.8.html)

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
