---
{"title": "newgidmap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/newgidmap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# newgidmap(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NEWGIDMAP(1)                  User Commands                  NEWGIDMAP(1)

## [](#NAME)NAME

           newgidmap - set the gid mapping of a user namespace

## [](#SYNOPSIS)SYNOPSIS

           newgidmap pid gid lowergid count [gid lowergid count [ ... ]]

## [](#DESCRIPTION)DESCRIPTION

           The newgidmap sets /proc/[pid]/gid_map based on its command line
           arguments and the gids allowed. Subgid delegation can either be
           managed via /etc/subgid or through the configured NSS subid
           module. These options are mutually exclusive.

           Note that the root group is not exempted from the requirement for
           a valid /etc/subgid entry.

           After the pid argument, newgidmap expects sets of 3 integers:

           gid
               Beginning of the range of GIDs inside the user namespace.

           lowergid
               Beginning of the range of GIDs outside the user namespace.

           count
               Length of the ranges (both inside and outside the user
               namespace).

           newgidmap verifies that the caller is the owner of the process
           indicated by pid and that for each of the above sets, each of the
           GIDs in the range [lowergid, lowergid+count) is allowed to the
           caller according to /etc/subgid before setting
           /proc/[pid]/gid_map.

           Note that newgidmap may be used only once for a given process.

           Instead of an integer process id, the first argument may be
           specified as fd:N, where the integer N is the file descriptor
           number for the calling process's opened file descriptor for the
           directory /proc/[pid]. In this case, newgidmap will use openat(2)
           to open the gid_map file under that directory, avoiding a TOCTTOU
           in case the process exits and the pid is immediately reused.

## [](#OPTIONS)OPTIONS

           There currently are no options to the newgidmap command.

## [](#FILES)FILES

           /etc/subgid
               List of user's subordinate group IDs.

           /proc/[pid]/gid_map
               Mapping of gids from one between user namespaces.

## [](#SEE_ALSO)SEE ALSO

           login.defs(5), newusers(8), subgid(5), useradd(8), userdel(8),
           usermod(8).

## [](#COLOPHON)COLOPHON

           This page is part of the shadow-utils (utilities for managing
           accounts and shadow password files) project.  Information about
           the project can be found at 
           ⟨https://github.com/shadow-maint/shadow⟩.  If you have a bug report
           for this manual page, send it to
           pkg-shadow-devel@alioth-lists.debian.net.  This page was obtained
           from the tarball shadow-4.19.0.tar fetched from
           ⟨https://github.com/shadow-maint/shadow/releases⟩ on 2026-08-04.
           If you discover any rendering problems in this HTML version of the
           page, or you believe there is a better or more up-to-date source
           for the page, or you have corrections or improvements to the
           information in this COLOPHON (which is not part of the original
           manual page), send a mail to man-pages@man7.org

    shadow-utils 4.19.0             08/04/2026                   NEWGIDMAP(1)

------------------------------------------------------------------------

Pages that refer to this page: [getsubids(1)](../man1/getsubids.1.html),  [unshare(1)](../man1/unshare.1.html),  [mount_setattr(2)](../man2/mount_setattr.2.html),  [subgid(5)](../man5/subgid.5.html),  [subuid(5)](../man5/subuid.5.html),  [user_namespaces(7)](../man7/user_namespaces.7.html)

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
