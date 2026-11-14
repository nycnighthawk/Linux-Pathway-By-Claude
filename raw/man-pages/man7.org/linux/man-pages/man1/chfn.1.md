---
{"title": "chfn(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/chfn.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# chfn(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONFIG FILE ITEMS](#CONFIG_FILE_ITEMS) \| [EXIT STATUS](#EXIT_STATUS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AVAILABILITY](#AVAILABILITY) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                              |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    CHFN(1)                       User Commands                       CHFN(1)

## [](#NAME)NAME

           chfn - change your finger information

## [](#SYNOPSIS)SYNOPSIS

           chfn [-f full-name] [-o office] [-p office-phone] [-h home-phone]
           [-u] [-V] [username|UID]

## [](#DESCRIPTION)DESCRIPTION

           chfn is used to change your finger information. This information
           is stored in the /etc/passwd file, and is displayed by the finger
           program. The Linux finger command will display four pieces of
           information that can be changed by chfn: your real name, your work
           room and phone, and your home phone.

           Any of the four pieces of information can be specified on the
           command line. If no information is given on the command line, chfn
           enters interactive mode.

           In interactive mode, chfn will prompt for each field. At a prompt,
           you can enter the new information, or just press return to leave
           the field unchanged. Enter the keyword "none" to make the field
           blank.

           chfn supports non-local entries (kerberos, LDAP, etc.) if linked
           with libuser, otherwise use ypchfn(1), lchfn(1) or any other
           implementation for non-local entries.

## [](#OPTIONS)OPTIONS

           -f, --full-name full-name
               Specify your real name.

           -o, --office office
               Specify your office room number.

           -p, --office-phone office-phone
               Specify your office phone number.

           -h, --home-phone home-phone
               Specify your home phone number.

           -u, --help
               Display help text and exit.

           -V, --version
               Display version and exit. (Short option -V is used since
               version 2.39; older versions used the now-deprecated -v).

## [](#CONFIG_FILE_ITEMS)CONFIG FILE ITEMS

           chfn reads the /etc/login.defs configuration file (see
           login.defs(5)). Note that the configuration file could be
           distributed with another package (e.g., shadow-utils). The
           following configuration items are relevant for chfn:

           CHFN_RESTRICT string
               Indicate which fields are changeable by chfn.

               The boolean setting "yes" means that only the Office, Office
               Phone and Home Phone fields are changeable, and boolean
               setting "no" means that also the Full Name is changeable.

               Another way to specify changeable fields is by abbreviations:

               f
                   Full Name

               r
                   Office (room)

               w
                   Office (work) Phone

               h
                   Home Phone

               For example, CHFN_RESTRICT "wh" allows changing work and home
               phone numbers.

               If CHFN_RESTRICT is undefined, then all finger information is
               read-only. This is the default.

## [](#EXIT_STATUS)EXIT STATUS

           Returns 0 if operation was successful, 1 if operation failed or
           command syntax was not valid.

## [](#AUTHORS)AUTHORS

           Salvatore Valente <svalente@mit.edu>, Christian Goeschel Ndjomouo
           <cgoesc2@wgu.edu>

## [](#SEE_ALSO)SEE ALSO

           chsh(1), finger(1), login.defs(5), passwd(5)

## [](#REPORTING_BUGS)REPORTING BUGS

           For bug reports, use the issue tracker
           <https://github.com/util-linux/util-linux/issues>.

## [](#AVAILABILITY)AVAILABILITY

           The chfn command is part of the util-linux package which can be
           downloaded from Linux Kernel Archive
           <https://www.kernel.org/pub/linux/utils/util-linux/>. This page is
           part of the util-linux (a random collection of Linux utilities)
           project. Information about the project can be found at 
           ⟨https://www.kernel.org/pub/linux/utils/util-linux/⟩. If you have a
           bug report for this manual page, send it to
           util-linux@vger.kernel.org. This page was obtained from the
           project's upstream Git repository
           ⟨git://git.kernel.org/pub/scm/utils/util-linux/util-linux.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-08-03.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    util-linux 2.43.devel-739-eee2e 2026-05-24                        CHFN(1)

------------------------------------------------------------------------

Pages that refer to this page: [chsh(1@@shadow-utils)](../man1/chsh.1@@shadow-utils.html),  [passwd(5)](../man5/passwd.5.html),  [groupadd(8)](../man8/groupadd.8.html),  [groupdel(8)](../man8/groupdel.8.html),  [groupmems(8)](../man8/groupmems.8.html),  [groupmod(8)](../man8/groupmod.8.html),  [useradd(8)](../man8/useradd.8.html),  [userdel(8)](../man8/userdel.8.html),  [usermod(8)](../man8/usermod.8.html)

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
