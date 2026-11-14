---
{"title": "captest(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/captest.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# captest(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CAPTEST:(8)          System Administration Utilities          CAPTEST:(8)

## [](#NAME)NAME

           captest - a program to demonstrate capabilities

## [](#SYNOPSIS)SYNOPSIS

           captest [ --ambient --drop-all | --drop-caps | --id ] [ --init-grp
           ] [ --lock ] [ --text ]

## [](#DESCRIPTION)DESCRIPTION

           captest is a program that demonstrates and prints out the current
           process capabilities. Each option prints the same report. It will
           output current capabilities. then it will try to access
           /etc/shadow directly to show if that can be done. Then it creates
           a child process that attempts to read /etc/shadow and outputs the
           results of that. Then it outputs the capabilities that a child
           process would have.

           You can also apply file system capabilities to this program to
           study how they work. For example, filecap /usr/bin/captest chown.
           Then run captest as a normal user. Another interesting test is to
           make captest suid root so that you can see what the interaction is
           between root's credentials and capabilities. For example, chmod
           4755 /usr/bin/captest. When run as a normal user, the program will
           see if privilege escalation is possible. But do not leave this app
           setuid root after you are done testing so that an attacker cannot
           take advantage of it.

## [](#OPTIONS)OPTIONS

           --ambient
                  This attempts to add CAP_CHOWN ambient capability.

           --drop-all
                  This drops all capabilities including ambient and clears
                  the bounding set.

           --drop-caps
                  This drops just traditional capabilities.

           --id   This changes to uid and gid 99, drops supplemental groups,
                  and clears the bounding set.

           --init-grp
                  This changes to uid and gid 99 and then adds any
                  supplemental groups that comes with that account. You would
                  have to add them prior to testing because by default there
                  are no supplemental groups on account 99.

           --text This option outputs the effective capabilities in text
                  rather than numerically.

           --lock This prevents the ability for child processes to regain
                  privileges if the uid is 0.

## [](#SEE_ALSO)SEE ALSO

           filecap(8), capabilities(7)

## [](#AUTHOR)AUTHOR

           Steve Grubb

## [](#COLOPHON)COLOPHON

           This page is part of the libcap-ng (capabilities commands and
           library (NG)) project.  Information about the project can be found
           at ⟨https://people.redhat.com/sgrubb/libcap-ng/⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           tarball fetched from
           ⟨https://people.redhat.com/sgrubb/libcap-ng/index.html⟩ on
           2026-08-04.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Red Hat                         March 2026                    CAPTEST:(8)

------------------------------------------------------------------------

Pages that refer to this page: [capabilities(7)](../man7/capabilities.7.html)

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
