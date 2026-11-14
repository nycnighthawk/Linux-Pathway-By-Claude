---
{"title": "mv(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/mv.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mv(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    MV(1)                         User Commands                         MV(1)

## [](#NAME)NAME

           mv - move (rename) files

## [](#SYNOPSIS)SYNOPSIS

           mv [OPTION]... [-T] SOURCE DEST
           mv [OPTION]... SOURCE... DIRECTORY
           mv [OPTION]... -t DIRECTORY SOURCE...

## [](#DESCRIPTION)DESCRIPTION

           Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.

           Mandatory arguments to long options are mandatory for short
           options too.

           --backup[=CONTROL]
                  make a backup of each existing destination file

           -b     like --backup but does not accept an argument

           --debug
                  explain how a file is copied.  Implies -v

           --exchange
                  exchange source and destination

           -f, --force
                  do not prompt before overwriting

           -i, --interactive
                  prompt before overwrite

           -n, --no-clobber
                  do not overwrite an existing file

           If you specify more than one of -i, -f, -n, only the final one
           takes effect.

           --no-copy
                  do not copy if renaming fails

           --strip-trailing-slashes
                  remove any trailing slashes from each SOURCE argument

           -S, --suffix=SUFFIX
                  override the usual backup suffix

           -t, --target-directory=DIRECTORY
                  move all SOURCE arguments into DIRECTORY

           -T, --no-target-directory
                  treat DEST as a normal file

           --update[=UPDATE]
                  control which existing files are updated;
                  UPDATE={all,none,none-fail,older(default)}

           -u     equivalent to --update[=older].  See below

           -v, --verbose
                  explain what is being done

           -Z, --context
                  set SELinux security context of destination file to default
                  type

           --help display this help and exit

           --version
                  output version information and exit

           UPDATE controls which existing files in the destination are
           replaced.  'all' is the default operation when an --update option
           is not specified, and results in all existing files in the
           destination being replaced.  'none' is like the --no-clobber
           option, in that no files in the destination are replaced, and
           skipped files do not induce a failure.  'none-fail' also ensures
           no files are replaced in the destination, but any skipped files
           are diagnosed and induce a failure.  'older' is the default
           operation when --update is specified, and results in files being
           replaced if they're older than the corresponding source file.

           The backup suffix is '~', unless set with --suffix or
           SIMPLE_BACKUP_SUFFIX.  The version control method may be selected
           via the --backup option or through the VERSION_CONTROL environment
           variable.  Here are the values:

           none, off
                  never make backups (even if --backup is given)

           numbered, t
                  make numbered backups

           existing, nil
                  numbered if numbered backups exist, simple otherwise

           simple, never
                  always make simple backups

## [](#AUTHOR)AUTHOR

           Written by Mike Parker, David MacKenzie, and Jim Meyering.

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

           rename(2)

           Full documentation <https://www.gnu.org/software/coreutils/mv>
           or available locally via: info '(coreutils) mv invocation'

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

    GNU coreutils 9.11              April 2026                          MV(1)

------------------------------------------------------------------------

Pages that refer to this page: [rename(1)](../man1/rename.1.html),  [sshfs(1)](../man1/sshfs.1.html),  [rename(2)](../man2/rename.2.html),  [inotify(7)](../man7/inotify.7.html),  [symlink(7)](../man7/symlink.7.html),  [lsof(8)](../man8/lsof.8.html)

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
