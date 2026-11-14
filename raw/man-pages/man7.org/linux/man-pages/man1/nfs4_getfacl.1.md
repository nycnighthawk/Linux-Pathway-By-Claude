---
{"title": "nfs4_getfacl(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/nfs4_getfacl.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfs4_getfacl(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [AUTHORS](#AUTHORS) \| [CONTACT](#CONTACT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NFS4_GETFACL(1)         NFSv4 Access Control Lists        NFS4_GETFACL(1)

## [](#NAME)NAME

           nfs4_getfacl - get NFSv4 file/directory access control lists

## [](#SYNOPSIS)SYNOPSIS

           nfs4_getfacl [-HR] file ...

## [](#DESCRIPTION)DESCRIPTION

           nfs4_getfacl will display the NFSv4 Access Control List (ACL) for
           the files given as arguments, provided they are on mounted NFSv4
           filesystems which support ACLs.

           If the -H/--more-help flag is specified, nfs4_getfacl will print
           some information about NFSv4 ACLs and the fields used in ACEs.

           If the -R/--recursive flag is specified, nfs4_getfacl will list
           the NFSv4 ACLs of all files and directories recursively.

           If the -c/--omit-header flag is specified, nfs4_getfacl will not
           display the comment header (Do not print filename).

           If the --dacl flag is specified, nfs4_getfacl will retrieve the
           dacl. This functionality is only available if the server supports
           NFSv4 minor version 1 or newer.

           If the --sacl flag is specified, nfs4_getfacl will retrieve the
           sacl. This functionality is only available if the server supports
           NFSv4 minor version 1 or newer.

           The output format for an NFSv4 file ACL, e.g., is:

                  # file: /somedir
                  A::OWNER@:rwatTnNcCy
                  A::alice@nfsdomain.org:rxtncy
                  A::bob@nfsdomain.org:rwadtTnNcCy
                  A:g:GROUP@:rtncy
                  D:g:GROUP@:waxTC
                  A::EVERYONE@:rtncy
                  D::EVERYONE@:waxTC

           In the example output above, the user `alice@nfsdomain.org' has
           the equivalent of "read" and "execute" permissions,
           `bob@nfsdomain.org' has "read" and "write", and both `GROUP@' and
           `EVERYONE@' have "read".

           The ACL listings of multiple files are separated by blank lines.

           Refer to the nfs4_acl(5) manpage for detailed information about
           NFSv4 ACL terminology and syntax.

## [](#AUTHORS)AUTHORS

           nfs4_getfacl was written by people at CITI, the Center for
           Information Technology Integration (http://www.citi.umich.edu ).
           This manpage was written by David Richter.

## [](#CONTACT)CONTACT

           Please send bug reports, feature requests, and comments to <linux-
           nfs@vger.kernel.org>.

## [](#SEE_ALSO)SEE ALSO

           nfs4_setfacl(1), nfs4_acl(5), RFC3530 (NFSv4.0), NFSv4.1 Minor
           Version Draft.

## [](#COLOPHON)COLOPHON

           This page is part of the nfs4-acl-tools (NFSv4 ACL tools) project.
           Information about the project can be found at 
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  If you have a bug
           report for this manual page, see
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.linux-nfs.org/projects/bfields/nfs4-acl-tools.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2022-11-22.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Linux                   version 0.3.4, August 2018        NFS4_GETFACL(1)

------------------------------------------------------------------------

Pages that refer to this page: [nfs4_setfacl(1)](../man1/nfs4_setfacl.1.html),  [nfs4_acl(5)](../man5/nfs4_acl.5.html)

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
