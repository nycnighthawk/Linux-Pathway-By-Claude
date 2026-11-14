---
{"title": "chown(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chown.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chown(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [AUTHOR](#AUTHOR) \| [REPORTING BUGS](#REPORTING_BUGS) \| [COPYRIGHT](#COPYRIGHT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                              |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHOWN(1)                      User Commands                      CHOWN(1)

## [](#NAME)NAME

           chown - change file owner and group

## [](#SYNOPSIS)SYNOPSIS

           chown [OPTION]... [OWNER][:[GROUP]] FILE...
           chown [OPTION]... --reference=RFILE FILE...

## [](#DESCRIPTION)DESCRIPTION

           This manual page documents the GNU version of chown.  chown
           changes the user and/or group ownership of each given file.  If
           only an owner (a user name or numeric user ID) is given, that user
           is made the owner of each given file, and the files' group is not
           changed.  If the owner is followed by a colon and a group name (or
           numeric group ID), with no spaces between them, the group
           ownership of the files is changed as well.  If a colon but no
           group name follows the user name, that user is made the owner of
           the files and the group of the files is changed to that user's
           login group.  If the colon and group are given, but the owner is
           omitted, only the group of the files is changed; in this case,
           chown performs the same function as chgrp.  If only a colon is
           given, or if the entire operand is empty, neither the owner nor
           the group is changed.

## [](#OPTIONS)OPTIONS

           Change the owner and/or group of each FILE to OWNER and/or GROUP.
           With --reference, change the owner and group of each FILE to those
           of RFILE.

           -c, --changes
                  like verbose but report only when a change is made

           -f, --silent, --quiet
                  suppress most error messages

           -v, --verbose
                  output a diagnostic for every file processed

           --dereference
                  affect the referent of each symbolic link (this is the
                  default), rather than the symbolic link itself

           -h, --no-dereference
                  affect symbolic links instead of any referenced file;
                  useful only on systems that can change the ownership of a
                  symlink

           --from=CURRENT_OWNER:CURRENT_GROUP
                  change the ownership of each file only if its current owner
                  and/or group match those specified here.  Either may be
                  omitted, in which case a match is not required for the
                  omitted attribute

           --no-preserve-root
                  do not treat '/' specially (the default)

           --preserve-root
                  fail to operate recursively on '/'

           --reference=RFILE
                  use RFILE's ownership rather than specifying values.  RFILE
                  is always dereferenced if a symbolic link.

           -R, --recursive
                  operate on files and directories recursively

           The following options modify how a hierarchy is traversed when the
           -R option is also specified.  If more than one is specified, only
           the final one takes effect. -P is the default.

           -H     if a command line argument is a symlink to a directory,
                  traverse it

           -L     traverse every symbolic link to a directory encountered

           -P     do not traverse any symbolic links

           --help display this help and exit

           --version
                  output version information and exit

           Owner is unchanged if missing.  Group is unchanged if missing, but
           changed to login group if implied by a ':' following a symbolic
           OWNER.  OWNER and GROUP may be numeric as well as symbolic.

## [](#EXAMPLES)EXAMPLES

           chown root /u
                  Change the owner of /u to "root".

           chown root:staff /u
                  Likewise, but also change its group to "staff".

           chown -hR root /u
                  Change the owner of /u and subfiles to "root".

## [](#AUTHOR)AUTHOR

           Written by David MacKenzie and Jim Meyering.

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

           chown(2)

           Full documentation <https://www.gnu.org/software/coreutils/chown>
           or available locally via: info '(coreutils) chown invocation'

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

    GNU coreutils 9.11              April 2026                       CHOWN(1)

------------------------------------------------------------------------

Pages that refer to this page: [chgrp(1)](../man1/chgrp.1.html),  [chown(2)](../man2/chown.2.html),  [fd(4)](../man4/fd.4.html),  [hd(4)](../man4/hd.4.html),  [initrd(4)](../man4/initrd.4.html),  [lp(4)](../man4/lp.4.html),  [mem(4)](../man4/mem.4.html),  [null(4)](../man4/null.4.html),  [ram(4)](../man4/ram.4.html),  [tty(4)](../man4/tty.4.html),  [ttyS(4)](../man4/ttyS.4.html),  [rpm-spec(5)](../man5/rpm-spec.5.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [symlink(7)](../man7/symlink.7.html),  [sm-notify(8)](../man8/sm-notify.8.html),  [start-stop-daemon(8)](../man8/start-stop-daemon.8.html),  [statd(8)](../man8/statd.8.html)

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
