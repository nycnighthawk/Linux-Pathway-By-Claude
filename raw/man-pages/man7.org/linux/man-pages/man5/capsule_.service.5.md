---
{"title": "capsule@.service(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/capsule@.service.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# capsule@.service(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CAPSULE@.SERVICE(5)          capsule@.service         CAPSULE@.SERVICE(5)

## [](#NAME)NAME

           capsule@.service - System unit for the capsule service manager

## [](#SYNOPSIS)SYNOPSIS

           capsule@NAME.service

## [](#DESCRIPTION)DESCRIPTION

           Service managers for capsules run in capsule@NAME.service system
           units, with the capsule name as the instance identifier. Capsules
           are way to run additional instances of the service manager, under
           dynamic user IDs, i.e. UIDs that are allocated when the capsule
           service manager is started, and released when it is stopped.

           In many ways capsule@.service is similar to the per-user
           user@.service service manager, but there are a few important
           distinctions:

           •   The capsule service manager utilizes DynamicUser= (see
               systemd.exec(5)) to allocate a new UID dynamically on
               invocation. The user name is automatically generated from the
               capsule name, by prefixing "c-". The UID is released when the
               service is terminated. The user service manager on the other
               hand operates under a statically allocated user ID that must
               be pre-existing, before the user service manager is invoked.

           •   User service managers register themselves with pam(8), capsule
               service managers do not.

           •   User service managers typically read their configuration from
               a $HOME directory below /home/, capsule service managers from
               a $HOME directory below /var/lib/capsules/.

           •   User service managers are collectively contained in the
               user.slice unit, capsule service managers in capsule.slice.
               Also see systemd.special(7).

           •   User service managers start the user unit default.target
               initially. Capsule service managers invoke the user unit
               capsule@.target instead.

           The capsule service manager and the capsule's bus broker can be
           reached via the --capsule= switch to systemctl(1), systemd-run(1)
           and busctl(1).

           New capsules can be started via a simple systemctl start
           capsule@NAME.service command, and stopped via systemctl stop
           capsule@NAME.service. Starting a capsule will implicitly create a
           home directory /var/lib/capsules/NAME/, if missing. A runtime
           directory is created as /run/capsules/NAME/. To remove these
           resources use systemctl clean capsule@NAME.service, for example
           with the --what=all switch.

           The capsule@.service unit invokes a systemd --user service manager
           process. This means unit files are looked for according to the
           sames rules as for regular user service managers, for example in
           /var/lib/capsules/NAME/.config/systemd/user/.

           Capsule names may be chosen freely by the user, however, they must
           be suitable as UNIX filenames (i.e. 255 characters max, and
           contain no "/"), and when prefixed with "c-" be suitable as a user
           name matching strict POSIX rules, see User/Group Name Syntax[1]
           for details.

           Added in version 256.

## [](#EXAMPLES)EXAMPLES

           Example 1. Create a new capsule, invoke two programs in it (one
           interactively), terminate it, and clean everything up

               # systemctl start capsule@tatze.service
               # systemd-run --capsule=tatze --unit=sleeptest.service sleep 999
               # systemctl --capsule=tatze status sleeptest.service
               # systemd-run -t --capsule=tatze bash
               # systemctl --capsule=tatze stop sleeptest.service
               # systemctl stop capsule@tatze.service
               # systemctl clean --all capsule@tatze.service

## [](#SEE_ALSO)SEE ALSO

           systemd(1), user@.service(5), systemd.service(5),
           systemd.slice(5), systemd.exec(5), systemd.special(7),
           systemctl(1), systemd-run(1), busctl(1), pam(8)

## [](#NOTES)NOTES

            1. User/Group Name Syntax
               https://systemd.io/USER_NAMES

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                     CAPSULE@.SERVICE(5)

------------------------------------------------------------------------

Pages that refer to this page: [busctl(1)](../man1/busctl.1.html),  [systemctl(1)](../man1/systemctl.1.html),  [systemd-run(1)](../man1/systemd-run.1.html),  [user@.service(5)](../man5/user@.service.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.special(7)](../man7/systemd.special.7.html)

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
