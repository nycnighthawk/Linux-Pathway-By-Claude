---
{"title": "group.conf(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/group.conf.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# group.conf(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GROUP.CONF(5)                Linux-PAM Manual               GROUP.CONF(5)

## [](#NAME)NAME

           group.conf - configuration file for the pam_group module

## [](#DESCRIPTION)DESCRIPTION

           The pam_group PAM module does not authenticate the user, but
           instead it grants group memberships (in the credential setting
           phase of the authentication module) to the user. Such memberships
           are based on the service they are applying for.

           For this module to function correctly there must be a correctly
           formatted /etc/security/group.conf file present. White spaces are
           ignored and lines maybe extended with '\' (escaped newlines). Text
           following a '#' is ignored to the end of the line.

           The syntax of the lines is as follows:

           services;ttys;users;times;groups

           The first field, the services field, is a logic list of PAM
           service names that the rule applies to.

           The second field, the tty field, is a logic list of terminal names
           that this rule applies to.

           The third field, the users field, is a logic list of users, or a
           UNIX group, or a netgroup of users to whom this rule applies.
           Group names are preceded by a '%' symbol, while netgroup names are
           preceded by a '@' symbol.

           A logic list namely means individual tokens that are optionally
           prefixed with '!' (logical not) and separated with '&' (logical
           and) and '|' (logical or).

           For these items the simple wildcard '*' may be used only once.
           With UNIX groups or netgroups no wildcards or logic operators are
           allowed.

           The times field is used to indicate "when" these groups are to be
           given to the user. The format here is a logic list of
           day/time-range entries. The days are specified by a sequence of
           two character entries, MoTuSa for example is Monday Tuesday and
           Saturday. Note that repeated days are unset MoMo = no day, and
           MoWk = all weekdays bar Monday. The two character combinations
           accepted are Mo Tu We Th Fr Sa Su Wk Wd Al, the last two being
           week-end days and all 7 days of the week respectively. As a final
           example, AlFr means all days except Friday.

           Each day/time-range can be prefixed with a '!' to indicate
           "anything but". The time-range part is two 24-hour times HHMM,
           separated by a hyphen, indicating the start and finish time (if
           the finish time is smaller than the start time it is deemed to
           apply on the following day).

           The groups field is a comma or space separated list of groups that
           the user inherits membership of. These groups are added if the
           previous fields are satisfied by the user's request.

           For a rule to be active, ALL of service+ttys+users must be
           satisfied by the applying process.

## [](#EXAMPLES)EXAMPLES

           These are some example lines which might be specified in
           /etc/security/group.conf.

           Running 'xsh' on tty* (any ttyXXX device), the user 'us' is given
           access to the floppy (through membership of the floppy group)

               xsh;tty*&!ttyp*;us;Al0000-2400;floppy

           Running 'xsh' on tty* (any ttyXXX device), the users 'sword',
           'pike' and 'shield' are given access to games (through membership
           of the floppy group) after work hours.

               xsh; tty* ;sword|pike|shield;!Wk0900-1800;games, sound
               xsh; tty* ;*;Al0900-1800;floppy

           Any member of the group 'admin' running 'xsh' on tty*, is granted
           access (at any time) to the group 'plugdev'

               xsh; tty* ;%admin;Al0000-2400;plugdev

## [](#SEE_ALSO)SEE ALSO

           pam_group(8), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_group was written by Andrew G. Morgan <morgan@kernel.org>.

## [](#COLOPHON)COLOPHON

           This page is part of the linux-pam (Pluggable Authentication
           Modules for Linux) project.  Information about the project can be
           found at ⟨http://www.linux-pam.org/⟩.  If you have a bug report
           for this manual page, see ⟨//www.linux-pam.org/⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/linux-pam/linux-pam.git⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-07-30.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Linux-PAM                       08/04/2026                  GROUP.CONF(5)

------------------------------------------------------------------------

Pages that refer to this page: [pam_group(8)](../man8/pam_group.8.html)

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
