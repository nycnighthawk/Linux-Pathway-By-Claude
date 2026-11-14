---
{"title": "chacl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chacl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chacl(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [CAUTIONS](#CAUTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                  |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHACL(1)                   Access Control Lists                  CHACL(1)

## [](#NAME)NAME

           chacl - change the access control list of a file or directory

## [](#SYNOPSIS)SYNOPSIS

           chacl acl pathname...
           chacl -b acl dacl pathname...
           chacl -d dacl pathname...
           chacl -R pathname...
           chacl -D pathname...
           chacl -B pathname...
           chacl -l pathname...
           chacl -r pathname...

## [](#DESCRIPTION)DESCRIPTION

           chacl is an IRIX-compatibility command, and is maintained for
           those users who are familiar with its use from either XFS or IRIX.
           Refer to the SEE ALSO section below for a description of tools
           which conform more closely to the (withdrawn draft) POSIX 1003.1e
           standard which describes Access Control Lists (ACLs).

           chacl changes the ACL(s) for a file or directory.  The ACL(s)
           specified are applied to each file in the pathname arguments.

           Each ACL is a string which is interpreted using the
           acl_from_text(3) routine.  These strings are made up of comma
           separated clauses each of which is of the form, tag:name:perm.
           Where tag can be:

           "user" (or "u")
                  indicating that the entry is a "user" ACL entry.

           "group" (or "g")
                  indicating that the entry is a "group" ACL entry.

           "other" (or "o")
                  indicating that the entry is an "other" ACL entry.

           "mask" (or "m")
                  indicating that the entry is a "mask" ACL entry.

           name is a string which is the user or group name for the ACL
           entry.  A null name in a user or group ACL entry indicates the
           file's owner or file's group.  perm is the string "rwx" where each
           of the entries may be replaced by a "-" indicating no access of
           that type, e.g. "r-x", "--x", "---".

## [](#OPTIONS)OPTIONS

           -b     Indicates that there are two ACLs to change, the first is
                  the file access ACL and the second the directory default
                  ACL.

           -d     Used to set only the default ACL of a directory.

           -R     Removes the file access ACL only.

           -D     Removes directory default ACL only.

           -B     Remove all ACLs.

           -l     Lists the access ACL and possibly the default ACL
                  associated with the specified files or directories.  This
                  option was added during the Linux port of XFS, and is not
                  IRIX compatible.

           -r     Set the access ACL recursively for each subtree rooted at
                  pathname(s).  This option was also added during the Linux
                  port of XFS, and is not compatible with IRIX.

## [](#EXAMPLES)EXAMPLES

           A minimum ACL:

             chacl u::rwx,g::r-x,o::r-- file

           The file ACL is set so that the file's owner has "rwx", the file's
           group has read and execute, and others have read only access to
           the file.

           An ACL that is not a minimum ACL, that is, one that specifies a
           user or group other than the file's owner or owner's group, must
           contain a mask entry:

             chacl u::rwx,g::r-x,o::r--,u:bob:r--,m::r-x file1 file2

           To set the default and access ACLs on newdir to be the same as on
           olddir, you could type:

             chacl -b `chacl -l olddir | \
                 sed -e 's/.*\[//' -e 's#/# #' -e 's/]$//'` newdir

## [](#CAUTIONS)CAUTIONS

           chacl can replace the existing ACL.  To add or delete entries, you
           must first do chacl -l to get the existing ACL, and use the output
           to form the arguments to chacl.

           Changing the permission bits of a file will change the file access
           ACL settings (see chmod(1)).  However, file creation mode masks
           (see umask(1)) will not affect the access ACL settings of files
           created using directory default ACLs.

           ACLs are filesystem extended attributes and hence are not
           typically archived or restored using the conventional archiving
           utilities.  See attr(5) for more information about extended
           attributes and see xfsdump(8) for a method of backing them up
           under XFS.

## [](#SEE_ALSO)SEE ALSO

           getfacl(1), setfacl(1), chmod(1), umask(1), acl_from_text(3),
           acl(5), xfsdump(8)

## [](#COLOPHON)COLOPHON

           This page is part of the acl (manipulating access control lists)
           project.  Information about the project can be found at 
           ⟨http://savannah.nongnu.org/projects/acl⟩.  If you have a bug
           report for this manual page, see
           ⟨http://savannah.nongnu.org/bugs/?group=acl⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.savannah.nongnu.org/acl.git⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-29.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    September 2001              ACL File Utilities                   CHACL(1)

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
