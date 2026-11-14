---
{"title": "cp(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/cp.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# cp(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CP(1)                         User Commands                         CP(1)

## [](#NAME)NAME

           cp - copy files and directories

## [](#SYNOPSIS)SYNOPSIS

           cp [OPTION]... [-T] SOURCE DEST
           cp [OPTION]... SOURCE... DIRECTORY
           cp [OPTION]... -t DIRECTORY SOURCE...

## [](#DESCRIPTION)DESCRIPTION

           Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

           Mandatory arguments to long options are mandatory for short
           options too.

           -a, --archive
                  same as -dR --preserve=all

           --attributes-only
                  don't copy the file data, just the attributes

           --backup[=CONTROL]
                  make a backup of each existing destination file

           -b     like --backup but does not accept an argument

           --copy-contents
                  copy contents of special files when recursive

           -d     same as --no-dereference --preserve=links

           --debug
                  explain how a file is copied.  Implies -v

           -f, --force
                  if an existing destination file cannot be opened, remove it
                  and try again (this option is ignored when the -n option is
                  also used)

           -i, --interactive
                  prompt before overwrite (overrides a previous -n option)

           -H     follow command-line symbolic links in SOURCE

           -L, --dereference
                  always follow symbolic links in SOURCE

           -P, --no-dereference
                  never follow symbolic links in SOURCE

           --keep-directory-symlink
                  follow existing symlinks to directories

           -l, --link
                  hard link files instead of copying

           -n, --no-clobber
                  (deprecated) silently skip existing files.  See also
                  --update

           -p     same as --preserve=mode,ownership,timestamps

           --preserve[=ATTR_LIST]
                  preserve the specified attributes

           --no-preserve=ATTR_LIST
                  don't preserve the specified attributes

           --parents
                  use full source file name under DIRECTORY

           -R, -r, --recursive
                  copy directories recursively

           --reflink[=WHEN]
                  control clone/CoW copies. See below

           --remove-destination
                  remove each existing destination file before attempting to
                  open it (contrast with --force)

           --sparse=WHEN
                  control creation of sparse files. See below

           --strip-trailing-slashes
                  remove any trailing slashes from each SOURCE argument

           -s, --symbolic-link
                  make symbolic links instead of copying

           -S, --suffix=SUFFIX
                  override the usual backup suffix

           -t, --target-directory=DIRECTORY
                  copy all SOURCE arguments into DIRECTORY

           -T, --no-target-directory
                  treat DEST as a normal file

           --update[=UPDATE]
                  control which existing files are updated;
                  UPDATE={all,none,none-fail,older(default)}

           -u     equivalent to --update[=older].  See below

           -v, --verbose
                  explain what is being done

           -x, --one-file-system
                  stay on this file system

           -Z     set SELinux security context of destination file to default
                  type

           --context[=CTX]
                  like -Z, or if CTX is specified then set the SELinux or
                  SMACK security context to CTX

           --help display this help and exit

           --version
                  output version information and exit

           ATTR_LIST is a comma-separated list of attributes. Attributes are
           'mode' for permissions (including any ACL and xattr permissions),
           'ownership' for user and group, 'timestamps' for file timestamps,
           'links' for hard links, 'context' for security context, 'xattr'
           for extended attributes, and 'all' for all attributes.

           By default, sparse SOURCE files are detected by a crude heuristic
           and the corresponding DEST file is made sparse as well.  That is
           the behavior selected by --sparse=auto.  Specify --sparse=always
           to create a sparse DEST file whenever the SOURCE file contains a
           long enough sequence of zero bytes.  Use --sparse=never to inhibit
           creation of sparse files.

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

           By default or with --reflink=auto, cp will try a lightweight copy,
           where the data blocks are copied only when modified, falling back
           to a standard copy if this is not possible.  With
           --reflink[=always] cp will fail if CoW is not supported, while
           --reflink=never ensures a standard copy is performed.

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

           As a special case, cp makes a backup of SOURCE when the force and
           backup options are given and SOURCE and DEST are the same name for
           an existing, regular file.

## [](#AUTHOR)AUTHOR

           Written by Torbjorn Granlund, David MacKenzie, and Jim Meyering.

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

           install(1)

           Full documentation <https://www.gnu.org/software/coreutils/cp>
           or available locally via: info '(coreutils) cp invocation'

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

    GNU coreutils 9.11              April 2026                          CP(1)

------------------------------------------------------------------------

Pages that refer to this page: [install(1)](../man1/install.1.html),  [pmlogcompress(1)](../man1/pmlogcompress.1.html),  [rsync(1)](../man1/rsync.1.html),  [cpuset(7)](../man7/cpuset.7.html),  [symlink(7)](../man7/symlink.7.html),  [e2image(8)](../man8/e2image.8.html),  [readprofile(8)](../man8/readprofile.8.html),  [swapon(8)](../man8/swapon.8.html)

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
