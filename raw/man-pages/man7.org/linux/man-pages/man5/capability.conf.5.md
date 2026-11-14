---
{"title": "capability.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/capability.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# capability.conf(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CAPABILITY.CONF(5)         File Formats Manual         CAPABILITY.CONF(5)

## [](#NAME)NAME

           capability.conf - pam_cap module configuration file

## [](#SYNOPSIS)SYNOPSIS

           /etc/security/capability.conf

## [](#DESCRIPTION)DESCRIPTION

           The syntax for lines in this configuration file is:

           # <-- ´#´ precedes a comment

           <IAB><SPACE><WHO>

           Where <IAB> refers to the text format for an inheritable IAB
           capability tuple, see cap_text_formats(7) , or the words all or
           none.

           The reserved word all does not grant all the inheritable
           capabilities, but acts as a simple pass-through for any prevailing
           IAB tuple capabilities. The reserved word none refers to an empty
           Inheritable capability set (and by extension an empty Ambient
           vector).

           Here <WHO> refers to the space separated PAM username values that
           will be granted the specified IAB tuple. A name prefixed with the
           character @ refers to the locally defined /etc/group etc users
           listed under that group name. An asterisk "*" can be used to
           denote all users.

           The parsing of the file chooses the first line that applies to the
           authenticating user, and attempts to apply that and only that.

           Examples of valid syntax are:

               # only root gets to keep what it had
               all                                root

               # this should fire for user beta only, who will have
               # cap_chown dropped from their bounding set.
               !cap_chown                         beta

               # the next one should snag the members of the ´three´ group
               # granting them cap_setuid and cap_chown
               cap_setuid,cap_chown               @three

               # this would apply to beta and gamma, but beta is already
               # granted a lack of cap_chown above. Further, if gamma is
               # in the ´three´ group, it would not reach this line.
               cap_chown                          beta gamma

               # members of the ´one´ group are granted the cap_setuid Inheritable
               # capability, but cap_chown is dropped from their bounding set.
               !cap_chown,cap_setuid              @one

               # user alpha gets an ambient capability (unless it is also
               # a member of the groups ´one´ or ´three´).
               ^cap_setuid                        alpha

               # user delta (if not a member of groups ´one´ and ´three´) will get
               # cap_chown and cap_setgid Ambient capabilities, but have cap_setuid
               # dropped from its bounding set.
               ^cap_chown,^cap_setgid,!cap_setuid delta

               # any remaining members of group ´four´ will get the cap_setuid
               # Inheritable capability.
               cap_setuid                         @four

## [](#SEE_ALSO)SEE ALSO

           pam_cap(8), cap_iab(3), cap_text_formats(7).

## [](#COLOPHON)COLOPHON

           This page is part of the libcap (capabilities commands and
           library) project.  Information about the project can be found at
           ⟨https://sites.google.com/site/fullycapable/⟩.  If you have a bug
           report for this manual page, send it to morgan@kernel.org (please
           put "libcap" in the Subject line).  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/libs/libcap/libcap.git/⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-30.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                    2025-03-19             CAPABILITY.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [cap_text_formats(7)](../man7/cap_text_formats.7.html),  [pam_cap(8)](../man8/pam_cap.8.html)

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
