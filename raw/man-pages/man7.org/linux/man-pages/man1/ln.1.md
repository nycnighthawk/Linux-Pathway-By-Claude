---
{"title": "ln(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/ln.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# ln(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LN(1)                         User Commands                         LN(1)

## [](#NAME)NAME

           ln - make links between files

## [](#SYNOPSIS)SYNOPSIS

           ln [OPTION]... [-T] TARGET LINK_NAME
           ln [OPTION]... TARGET
           ln [OPTION]... TARGET... DIRECTORY
           ln [OPTION]... -t DIRECTORY TARGET...

## [](#DESCRIPTION)DESCRIPTION

           In the 1st form, create a link to TARGET with the name LINK_NAME.
           In the 2nd form, create a link to TARGET in the current directory.
           In the 3rd and 4th forms, create links to each TARGET in
           DIRECTORY.  Create hard links by default, symbolic links with
           --symbolic.  By default, each destination (name of new link)
           should not already exist.  When creating hard links, each TARGET
           must exist.  Symbolic links can hold arbitrary text; if later
           resolved, a relative link is interpreted in relation to its parent
           directory.

           Mandatory arguments to long options are mandatory for short
           options too.

           --backup[=CONTROL]
                  make a backup of each existing destination file

           -b     like --backup but does not accept an argument

           -d, -F, --directory
                  allow the superuser to attempt to hard link directories, if
                  supported by the system

           -f, --force
                  remove existing destination files

           -i, --interactive
                  prompt whether to remove destinations

           -L, --logical
                  dereference TARGETs that are symbolic links

           -n, --no-dereference
                  treat LINK_NAME as a normal file if it is a symbolic link
                  to a directory

           -P, --physical
                  make hard links directly to symbolic links

           -r, --relative
                  with -s, create links relative to link location

           -s, --symbolic
                  make symbolic links instead of hard links

           -S, --suffix=SUFFIX
                  override the usual backup suffix

           -t, --target-directory=DIRECTORY
                  specify the DIRECTORY in which to create the links

           -T, --no-target-directory
                  treat LINK_NAME as a normal file always

           -v, --verbose
                  print name of each linked file

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

           Using -s ignores -L and -P.  Otherwise, the last option specified
           controls behavior when a TARGET is a symbolic link, defaulting to
           -P.

## [](#AUTHOR)AUTHOR

           Written by Mike Parker and David MacKenzie.

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

           link(2), symlink(2)

           Full documentation <https://www.gnu.org/software/coreutils/ln>
           or available locally via: info '(coreutils) ln invocation'

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

    GNU coreutils 9.11              April 2026                          LN(1)

------------------------------------------------------------------------

Pages that refer to this page: [dh_link(1)](../man1/dh_link.1.html),  [pmlogcompress(1)](../man1/pmlogcompress.1.html),  [update-alternatives(1)](../man1/update-alternatives.1.html),  [link(2)](../man2/link.2.html),  [symlink(2)](../man2/symlink.2.html),  [hier(7)](../man7/hier.7.html),  [symlink(7)](../man7/symlink.7.html),  [sln(8)](../man8/sln.8.html)

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
