---
{"title": "install(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/install.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# install(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    INSTALL(1)                    User Commands                    INSTALL(1)

## [](#NAME)NAME

           install - copy files and set attributes

## [](#SYNOPSIS)SYNOPSIS

           install [OPTION]... [-T] SOURCE DEST
           install [OPTION]... SOURCE... DIRECTORY
           install [OPTION]... -t DIRECTORY SOURCE...
           install [OPTION]... -d DIRECTORY...

## [](#DESCRIPTION)DESCRIPTION

           This install program copies files (often just compiled) into
           destination locations you choose.  If you want to download and
           install a ready-to-use package on a GNU/Linux system, you should
           instead be using a package manager like yum(1) or apt-get(1).

           In the first three forms, copy SOURCE to DEST or multiple
           SOURCE(s) to the existing DIRECTORY, while setting permission
           modes and owner/group.  In the 4th form, create all components of
           the given DIRECTORY(ies).

           Mandatory arguments to long options are mandatory for short
           options too.

           --backup[=CONTROL]
                  make a backup of each existing destination file

           -b     like --backup but does not accept an argument

           -c     (ignored)

           -C, --compare
                  compare content of source and destination files, and if no
                  change to content, ownership, and permissions, do not
                  modify the destination at all

           -d, --directory
                  treat all arguments as directory names; create all
                  components of the specified directories

           -D     create all leading components of DEST except the last, or
                  all components of --target-directory, then copy SOURCE to
                  DEST

           --debug
                  explain how a file is copied.  Implies -v

           -g, --group=GROUP
                  set group ownership, instead of process' current group

           -m, --mode=MODE
                  set permission mode (as in chmod), instead of rwxr-xr-x

           -o, --owner=OWNER
                  set ownership (super-user only)

           -p, --preserve-timestamps
                  apply access/modification times of SOURCE files to
                  corresponding destination files

           -s, --strip
                  strip symbol tables

           --strip-program=PROGRAM
                  program used to strip binaries

           -S, --suffix=SUFFIX
                  override the usual backup suffix

           -t, --target-directory=DIRECTORY
                  copy all SOURCE arguments into DIRECTORY

           -T, --no-target-directory
                  treat DEST as a normal file

           -v, --verbose
                  print the name of each created file or directory

           --preserve-context
                  preserve SELinux security context

           -Z     set SELinux security context of destination file and each
                  created directory, to default type

           --context[=CTX]
                  like -Z, or if CTX is specified then set the SELinux or
                  SMACK security context to CTX

           --help display this help and exit

           --version
                  output version information and exit

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

           Written by David MacKenzie.

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

           cp(1)

           Full documentation
           <https://www.gnu.org/software/coreutils/install>
           or available locally via: info '(coreutils) install invocation'

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

    GNU coreutils 9.11              April 2026                     INSTALL(1)

------------------------------------------------------------------------

Pages that refer to this page: [cp(1)](../man1/cp.1.html)

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
