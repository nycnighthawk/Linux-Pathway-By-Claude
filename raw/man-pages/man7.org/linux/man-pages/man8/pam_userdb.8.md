---
{"title": "pam_userdb(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_userdb.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_userdb(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_USERDB(8)                Linux-PAM Manual               PAM_USERDB(8)

## [](#NAME)NAME

           pam_userdb - PAM module to authenticate against a db database

## [](#SYNOPSIS)SYNOPSIS

           pam_userdb.so db=/path/database [debug] [crypt=[crypt|none]]
                         [icase] [dump] [try_first_pass] [use_first_pass]
                         [unknown_ok] [key_only]

## [](#DESCRIPTION)DESCRIPTION

           The pam_userdb module is used to verify a username/password pair
           against values stored in a Berkeley DB database. The database is
           indexed by the username, and the data fields corresponding to the
           username keys are the passwords.

## [](#OPTIONS)OPTIONS

           crypt=[crypt|none]
               Indicates whether encrypted or plaintext passwords are stored
               in the database. If it is crypt, passwords should be stored in
               the database in crypt(3) form. If none is selected, passwords
               should be stored in the database as plaintext.

           db=/path/database
               Use the /path/database database for performing lookup. There
               is no default; the module will return PAM_IGNORE if no
               database is provided. Note that the path to the database file
               should be specified without the .db suffix.

           debug
               Print debug information. Note that password hashes, both from
               db and computed, will be printed to syslog.

           dump
               Dump all the entries in the database to the log. Don't do this
               by default!

           icase
               Make the password verification to be case insensitive (ie when
               working with registration numbers and such). Only works with
               plaintext password storage.

           try_first_pass
               Use the authentication token previously obtained by another
               module that did the conversation with the application. If this
               token can not be obtained then the module will try to
               converse. This option can be used for stacking different
               modules that need to deal with the authentication tokens.

           use_first_pass
               Use the authentication token previously obtained by another
               module that did the conversation with the application. If this
               token can not be obtained then the module will fail. This
               option can be used for stacking different modules that need to
               deal with the authentication tokens.

           unknown_ok
               Do not return error when checking for a user that is not in
               the database. This can be used to stack more than one
               pam_userdb module that will check a username/password pair in
               more than a database.

           key_only
               The username and password are concatenated together in the
               database hash as 'username-password' with a random value. if
               the concatenation of the username and password with a dash in
               the middle returns any result, the user is valid. this is
               useful in cases where the username may not be unique but the
               username and password pair are.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           The auth and account module types are provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               Authentication failure.

           PAM_AUTHTOK_RECOVERY_ERR
               Authentication information cannot be recovered.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_CONV_ERR
               Conversation failure.

           PAM_SERVICE_ERR
               Error in service module.

           PAM_SUCCESS
               Success.

           PAM_USER_UNKNOWN
               User not known to the underlying authentication module.

## [](#EXAMPLES)EXAMPLES

               auth  sufficient pam_userdb.so icase db=/etc/dbtest

## [](#SEE_ALSO)SEE ALSO

           crypt(3), pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_userdb was written by Cristian Gafton >gafton@redhat.com<.

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

    Linux-PAM                       08/04/2026                  PAM_USERDB(8)

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
