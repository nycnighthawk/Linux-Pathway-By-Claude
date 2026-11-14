---
{"title": "pam_listfile(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_listfile.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_listfile(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [MODULE TYPES PROVIDED](#MODULE_TYPES_PROVIDED) \| [RETURN VALUES](#RETURN_VALUES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_LISTFILE(8)              Linux-PAM Manual             PAM_LISTFILE(8)

## [](#NAME)NAME

           pam_listfile - deny or allow services based on an arbitrary file

## [](#SYNOPSIS)SYNOPSIS

           pam_listfile.so item=[tty|user|rhost|ruser|group|shell]
                           sense=[allow|deny] file=/path/filename
                           onerr=[succeed|fail] [apply=[user|@group]] [quiet]

## [](#DESCRIPTION)DESCRIPTION

           pam_listfile is a PAM module which provides a way to deny or allow
           services based on an arbitrary file.

           The module gets the item of the type specified -- user specifies
           the username, PAM_USER; tty specifies the name of the terminal (if
           any) over which the request has been made, PAM_TTY; rhost
           specifies the name of the remote host (if any) from which the
           request was made, PAM_RHOST; and ruser specifies the name of the
           remote user (if available) who made the request, PAM_RUSER -- and
           looks for an instance of that item in the file=filename.  filename
           contains one line per item listed. If the item is found, then if
           sense=allow, PAM_SUCCESS is returned, causing the authorization
           request to succeed; else if sense=deny, PAM_AUTH_ERR is returned,
           causing the authorization request to fail.

           If an error is encountered (for instance, if filename does not
           exist, or a poorly-constructed argument is encountered), then if
           onerr=succeed, PAM_SUCCESS is returned, otherwise if onerr=fail,
           PAM_AUTH_ERR or PAM_SERVICE_ERR (as appropriate) will be returned.

           An additional argument, apply=, can be used to restrict the
           application of the above to a specific user (apply=username) or a
           given group (apply=@groupname). This added restriction is only
           meaningful when used with the tty, rhost and shell items.

           Besides this last one, all arguments should be specified; do not
           count on any default behavior.

           No credentials are awarded by this module.

## [](#OPTIONS)OPTIONS

           item=[tty|user|rhost|ruser|group|shell]
               What is listed in the file and should be checked for.

           sense=[allow|deny]
               Action to take if the item is found in the file. If the item
               is NOT found in the file, then the opposite action is
               requested.

           file=/path/filename
               File containing one item per line. The file needs to be a
               plain file and not world writable.

           onerr=[succeed|fail]
               What to do if something weird happens like being unable to
               open the file.

           apply=[user|@group]
               Restrict the user class for which the restriction apply. Note
               that with item=[user|ruser|group] this does not make sense,
               but for item=[tty|rhost|shell] it has a meaning.

           quiet
               Do not treat service refusals or missing list files as errors
               that need to be logged.

## [](#MODULE_TYPES_PROVIDED)MODULE TYPES PROVIDED

           All module types (auth, account, password and session) are
           provided.

## [](#RETURN_VALUES)RETURN VALUES

           PAM_AUTH_ERR
               Authentication failure.

           PAM_BUF_ERR
               Memory buffer error.

           PAM_IGNORE
               The rule does not apply to the apply option.

           PAM_SERVICE_ERR
               Error in service module.

           PAM_SUCCESS
               Success.

## [](#EXAMPLES)EXAMPLES

           Classic 'ftpusers' authentication can be implemented with this
           entry in /etc/pam.d/ftpd:

               #
               # deny ftp-access to users listed in the /etc/ftpusers file
               #
               auth    required       pam_listfile.so \
                       onerr=succeed item=user sense=deny file=/etc/ftpusers

           Note, users listed in /etc/ftpusers file are (counterintuitively)
           not allowed access to the ftp service.

           To allow login access only for certain users, you can use a
           /etc/pam.d/login entry like this:

               #
               # permit login to users listed in /etc/loginusers
               #
               auth    required       pam_listfile.so \
                       onerr=fail item=user sense=allow file=/etc/loginusers

           For this example to work, all users who are allowed to use the
           login service should be listed in the file /etc/loginusers. Unless
           you are explicitly trying to lock out root, make sure that when
           you do this, you leave a way for root to log in, either by listing
           root in /etc/loginusers, or by listing a user who is able to su to
           the root account.

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), pam.d(5), pam(8)

## [](#AUTHOR)AUTHOR

           pam_listfile was written by Michael K. Johnson
           <johnsonm@redhat.com> and Elliot Lee <sopwith@cuc.edu>.

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

    Linux-PAM                       08/04/2026                PAM_LISTFILE(8)

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
