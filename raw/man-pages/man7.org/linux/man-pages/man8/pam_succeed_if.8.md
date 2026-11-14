---
{"title": "pam_succeed_if(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_succeed_if.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_succeed_if(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_SUCCEED_IF(8)            Linux-PAM Manual           PAM_SUCCEED_IF(8)

## [](#NAME)NAME

           pam_succeed_if - test account characteristics

## [](#SYNOPSIS)SYNOPSIS

           pam_succeed_if.so [flag...] [condition...]

## [](#DESCRIPTION)DESCRIPTION

           pam_succeed_if.so is designed to succeed or fail authentication
           based on characteristics of the account belonging to the user
           being authenticated or values of other PAM items. One use is to
           select whether to load other modules based on this test.

           The module should be given one or more conditions as module
           arguments, and authentication will succeed only if all of the
           conditions are met.

## [](#OPTIONS)OPTIONS

           The following flags are supported:

           debug
               Turns on debugging messages sent to syslog.

           use_uid
               Evaluate conditions using the account of the user whose UID
               the application is running under instead of the user being
               authenticated.

           quiet
               Don't log failure or success to the system log.

           quiet_fail
               Don't log failure to the system log.

           quiet_success
               Don't log success to the system log.

           audit
               Log unknown users to the system log.

           Conditions are three words: a field, a test, and a value to test
           for.

           Available fields are user, uid, gid, shell, home, ruser, rhost,
           tty and service:

           field < number
               Field has a value numerically less than number.

           field <= number
               Field has a value numerically less than or equal to number.

           field eq number
               Field has a value numerically equal to number.

           field >= number
               Field has a value numerically greater than or equal to number.

           field > number
               Field has a value numerically greater than number.

           field ne number
               Field has a value numerically different from number.

           field = string
               Field exactly matches the given string.

           field != string
               Field does not match the given string.

           field =~ glob
               Field matches the given glob.

           field !~ glob
               Field does not match the given glob.

           field in item:item:...
               Field is contained in the list of items separated by colons.

           field notin item:item:...
               Field is not contained in the list of items separated by
               colons.

           user ingroup group[:group:....]
               User is in given group(s).

           user notingroup group[:group:....]
               User is not in given group(s).

           user innetgr netgroup
               (user,host) is in given netgroup.

           user notinnetgr group
               (user,host) is not in given netgroup.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (account, auth, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_SUCCESS
               The condition was true.

           PAM_AUTH_ERR
               The condition was false.

           PAM_SERVICE_ERR
               A service error occurred or the arguments can't be parsed
               correctly.

## [](#EXAMPLES)EXAMPLES

           To emulate the behaviour of pam_wheel, except there is no fallback
           to group 0 being only approximated by checking also the root group
           membership:

               auth required pam_succeed_if.so quiet user ingroup wheel:root

           Given that the type matches, only loads the othermodule rule if
           the UID is over 500. Adjust the number after default to skip
           several rules.

               type [default=1 success=ignore] pam_succeed_if.so quiet uid > 500
               type required othermodule.so arguments...

## [](#SEE_ALSO)SEE ALSO

           glob(7), pam(8)

## [](#AUTHOR)AUTHOR

           Nalin Dahyabhai <nalin@redhat.com>

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

    Linux-PAM                       08/04/2026              PAM_SUCCEED_IF(8)

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
