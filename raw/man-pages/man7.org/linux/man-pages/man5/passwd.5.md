---
{"title": "passwd(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/passwd.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# passwd(5) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    passwd(5)                  File Formats Manual                  passwd(5)

## [](#NAME)NAME

           passwd - password file

## [](#DESCRIPTION)DESCRIPTION

           The /etc/passwd file is a text file that describes user login
           accounts for the system.  It should have read permission allowed
           for all users (many utilities, like ls(1) use it to map user IDs
           to usernames), but write access only for the superuser.

           In the good old days there was no great problem with this general
           read permission.  Everybody could read the encrypted passwords,
           but the hardware was too slow to crack a well-chosen password, and
           moreover the basic assumption used to be that of a friendly user-
           community.  These days many people run some version of the shadow
           password suite, where /etc/passwd has an 'x' character in the
           password field, and the encrypted passwords are in /etc/shadow,
           which is readable by the superuser only.

           If the encrypted password, whether in /etc/passwd or in
           /etc/shadow, is an empty string, login is allowed without even
           asking for a password.  Note that this functionality may be
           intentionally disabled in applications, or configurable (for
           example using the "nullok" or "nonull" arguments to pam_unix(8)).

           If the encrypted password in /etc/passwd is "*NP*" (without the
           quotes), the shadow record should be obtained from an NIS+ server.

           Regardless of whether shadow passwords are used, many system
           administrators use an asterisk (*) in the encrypted password field
           to make sure that this user can not authenticate themself using a
           password.  (But see NOTES below.)

           If you create a new login, first put an asterisk (*) in the
           password field, then use passwd(1) to set it.

           Each line of the file describes a single user, and contains seven
           colon-separated fields:

               name:password:UID:GID:GECOS:directory:shell

           The field are as follows:

           name   This is the user's login name.  It should not contain
                  capital letters.

           password
                  This is either the encrypted user password, an asterisk
                  (*), or the letter 'x'.  (See pwconv(8) for an explanation
                  of 'x'.)

           UID    The privileged root login account (superuser) has the user
                  ID 0.

           GID    This is the numeric primary group ID for this user.
                  (Additional groups for the user are defined in the system
                  group file; see group(5)).

           GECOS  This field (sometimes called the "comment field") is
                  optional and used only for informational purposes.
                  Usually, it contains the full username.  Some programs (for
                  example, finger(1)) display information from this field.

                  GECOS stands for "General Electric Comprehensive Operating
                  System", which was renamed to GCOS when GE's large systems
                  division was sold to Honeywell.  Dennis Ritchie has
                  reported: "Sometimes we sent printer output or batch jobs
                  to the GCOS machine.  The gcos field in the password file
                  was a place to stash the information for the $IDENTcard.
                  Not elegant."

           directory
                  This is the user's home directory: the initial directory
                  where the user is placed after logging in.  The value in
                  this field is used to set the HOME environment variable.

           shell  This is the program to run at login (if empty, use
                  /bin/sh).  If set to a nonexistent executable, the user
                  will be unable to login through login(1).  The value in
                  this field is used to set the SHELL environment variable.

## [](#FILES)FILES

           /etc/passwd

## [](#NOTES)NOTES

           If you want to create user groups, there must be an entry in
           /etc/group, or no group will exist.

           If the encrypted password is set to an asterisk (*), the user will
           be unable to login using login(1), but may still login using
           rlogin(1), run existing processes and initiate new ones through
           rsh(1), cron(8), at(1), or mail filters, etc.  Trying to lock an
           account by simply changing the shell field yields the same result
           and additionally allows the use of su(1).

## [](#SEE_ALSO)SEE ALSO

           chfn(1), chsh(1), login(1), passwd(1), su(1), crypt(3),
           getpwent(3), getpwnam(3), group(5), shadow(5), vipw(8)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2025-09-21                      passwd(5)

------------------------------------------------------------------------

Pages that refer to this page: [chage(1)](../man1/chage.1.html),  [chfn(1)](../man1/chfn.1.html),  [chfn(1@@shadow-utils)](../man1/chfn.1@@shadow-utils.html),  [chsh(1)](../man1/chsh.1.html),  [chsh(1@@shadow-utils)](../man1/chsh.1@@shadow-utils.html),  [expiry(1)](../man1/expiry.1.html),  [indomcachectl(1)](../man1/indomcachectl.1.html),  [login(1)](../man1/login.1.html),  [login(1@@shadow-utils)](../man1/login.1@@shadow-utils.html),  [lslogins(1)](../man1/lslogins.1.html),  [passwd(1)](../man1/passwd.1.html),  [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [crypt(3)](../man3/crypt.3.html),  [fgetpwent(3)](../man3/fgetpwent.3.html),  [getgrouplist(3)](../man3/getgrouplist.3.html),  [getpw(3)](../man3/getpw.3.html),  [getpwent(3)](../man3/getpwent.3.html),  [getpwent_r(3)](../man3/getpwent_r.3.html),  [getpwnam(3)](../man3/getpwnam.3.html),  [sysexits.h(3head)](../man3/sysexits.h.3head.html),  [ftpusers(5)](../man5/ftpusers.5.html),  [group(5)](../man5/group.5.html),  [login.defs(5)](../man5/login.defs.5.html),  [rpm-config(5)](../man5/rpm-config.5.html),  [shadow(5)](../man5/shadow.5.html),  [slapd.backends(5)](../man5/slapd.backends.5.html),  [slapd-passwd(5)](../man5/slapd-passwd.5.html),  [systemd.exec(5)](../man5/systemd.exec.5.html),  [credentials(7)](../man7/credentials.7.html),  [environ(7)](../man7/environ.7.html),  [rpm-lua(7)](../man7/rpm-lua.7.html),  [grpck(8)](../man8/grpck.8.html),  [newusers(8)](../man8/newusers.8.html),  [nologin(8)](../man8/nologin.8.html),  [nscd(8)](../man8/nscd.8.html),  [pwck(8)](../man8/pwck.8.html),  [rpm(8)](../man8/rpm.8.html),  [rpm-common(8)](../man8/rpm-common.8.html),  [vipw(8)](../man8/vipw.8.html)

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
