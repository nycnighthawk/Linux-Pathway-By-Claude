---
{"title": "subuid(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/subuid.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# subuid(5) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [LOCAL SUBORDINATE DELEGATION](#LOCAL_SUBORDINATE_DELEGATION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SUBUID(5)             File Formats and Configuration            SUBUID(5)

## [](#NAME)NAME

           subuid - the configuration for subordinate user ids

## [](#DESCRIPTION)DESCRIPTION

           Subuid authorizes a user id to map ranges of user ids from its
           namespace into child namespaces.

           The delegation of the subordinate uids can be configured via the
           subid field in /etc/nsswitch.conf file. Only one value can be set
           as the delegation source. Setting this field to files configures
           the delegation of uids to /etc/subuid. Setting any other value
           treats the delegation as a plugin following with a name of the
           form libsubid_$value.so. If the value or plugin is missing, then
           the subordinate uid delegation falls back to files.

           Note, that newusers, useradd, and usermod will only create entries
           in /etc/subuid if subid delegation is managed via subid files.

## [](#LOCAL_SUBORDINATE_DELEGATION)LOCAL SUBORDINATE DELEGATION

           Each line in /etc/subuid contains a user name and a range of
           subordinate user ids that user is allowed to use. This is
           specified with three fields delimited by colons (“:”). These
           fields are:

           •   login name or UID

           •   numerical subordinate user ID

           •   numerical subordinate user ID count

           This file specifies the user IDs that ordinary users can use, with
           the newuidmap command, to configure uid mapping in a user
           namespace.

           Multiple ranges may be specified per user.

           When large number of entries (10000-100000 or more) are defined in
           /etc/subuid, parsing performance penalty will become noticeable.
           In this case it is recommended to use UIDs instead of login names.
           Benchmarks have shown speed-ups up to 20x.

## [](#FILES)FILES

           /etc/subuid
               Per user subordinate user IDs.

           /etc/subuid-
               Backup file for /etc/subuid.

## [](#SEE_ALSO)SEE ALSO

           login.defs(5), newgidmap(1), newuidmap(1), newusers(8), subgid(5),
           useradd(8), userdel(8), usermod(8), user_namespaces(7).

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

    shadow-utils 4.19.0             08/04/2026                      SUBUID(5)

------------------------------------------------------------------------

Pages that refer to this page: [getsubids(1)](../man1/getsubids.1.html),  [newuidmap(1)](../man1/newuidmap.1.html),  [unshare(1)](../man1/unshare.1.html),  [nsswitch.conf(5)](../man5/nsswitch.conf.5.html),  [subgid(5)](../man5/subgid.5.html),  [user_namespaces(7)](../man7/user_namespaces.7.html),  [newusers(8)](../man8/newusers.8.html),  [useradd(8)](../man8/useradd.8.html),  [userdel(8)](../man8/userdel.8.html),  [usermod(8)](../man8/usermod.8.html)

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
