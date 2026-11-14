---
{"title": "newuidmap(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/newuidmap.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# newuidmap(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NEWUIDMAP(1)                  User Commands                  NEWUIDMAP(1)

## [](#NAME)NAME

           newuidmap - set the uid mapping of a user namespace

## [](#SYNOPSIS)SYNOPSIS

           newuidmap pid uid loweruid count [uid loweruid count [ ... ]]

## [](#DESCRIPTION)DESCRIPTION

           The newuidmap sets /proc/[pid]/uid_map based on its command line
           arguments and the uids allowed. Subuid delegation can either be
           managed via /etc/subuid or through the configured NSS subid
           module. These options are mutually exclusive.

           Note that the root user is not exempted from the requirement for a
           valid /etc/subuid entry.

           After the pid argument, newuidmap expects sets of 3 integers:

           uid
               Beginning of the range of UIDs inside the user namespace.

           loweruid
               Beginning of the range of UIDs outside the user namespace.

           count
               Length of the ranges (both inside and outside the user
               namespace).

           newuidmap verifies that the caller is the owner of the process
           indicated by pid and that for each of the above sets, each of the
           UIDs in the range [loweruid, loweruid+count) is allowed to the
           caller according to /etc/subuid before setting
           /proc/[pid]/uid_map.

           Note that newuidmap may be used only once for a given process.

           Instead of an integer process id, the first argument may be
           specified as fd:N, where the integer N is the file descriptor
           number for the calling process's opened file descriptor for the
           directory /proc/[pid]. In this case, newuidmap will use openat(2)
           to open the uid_map file under that directory, avoiding a TOCTTOU
           in case the process exits and the pid is immediately reused.

## [](#OPTIONS)OPTIONS

           There currently are no options to the newuidmap command.

## [](#FILES)FILES

           /etc/subuid
               List of user's subordinate user IDs.

           /proc/[pid]/uid_map
               Mapping of uids from one between user namespaces.

## [](#SEE_ALSO)SEE ALSO

           login.defs(5), newusers(8), subuid(5), useradd(8), usermod(8),
           userdel(8).

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

    shadow-utils 4.19.0             08/04/2026                   NEWUIDMAP(1)

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
