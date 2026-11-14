---
{"title": "request-key(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/request-key.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# request-key(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                 |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    REQUEST-KEY(8)        Linux Key Management Utilities       REQUEST-KEY(8)

## [](#NAME)NAME

           request-key - handle key instantiation callback requests from the
           kernel

## [](#SYNOPSIS)SYNOPSIS

           /sbin/request-key <op> <key> <uid> <gid> <threadring>
           <processring>      <sessionring> [<info>]

## [](#DESCRIPTION)DESCRIPTION

           This program is invoked by the kernel when the kernel is asked for
           a key that it doesn't have immediately available. The kernel
           creates a partially set up key and then calls out to this program
           to instantiate it. It is not intended to be called directly.

           However, for debugging purposes, it can be given some options on
           the command line:

           -d     Turn on debugging mode.  In this mode, no attempts are made
                  to access any keys and, if a handler program is selected,
                  it won't be executed; instead, this program will print a
                  message and exit 0.

           -D     In debugging mode, use the proposed key description
                  specified with this rather than the sample
                  ("user;0;0;1f0000;debug:1234") built into the program.

           -l     Use configuration from the current directory.  The program
                  will use request-key.d/* and request-key.conf from the
                  current directory rather than from /etc.

           -n     Don't log to the system log.  Ordinarily, error messages
                  and debugging messages will be copied to the system log -
                  this will prevent that.

           -v     Turn on debugging output.  This may be specified multiple
                  times to produce increasing levels of verbosity.

           --version
                  Print the program version and exit.

## [](#ERRORS)ERRORS

           All errors will be logged to the syslog.

## [](#FILES)FILES

           /etc/request-key.d/*.conf Individual configuration files.

           /etc/request-key.conf Fallback configuration file.

## [](#SEE_ALSO)SEE ALSO

           keyctl(1), request-key.conf(5), keyrings(7)

## [](#COLOPHON)COLOPHON

           This page is part of the keyutils (key management utilities)
           project.  Information about the project can be found at [unknown
           -- if you know, please contact man-pages@man7.org] If you have a
           bug report for this manual page, send it to
           keyrings@linux-nfs.org.  This page was obtained from the project's
           upstream Git repository
           ⟨http://git.kernel.org/pub/scm/linux/kernel/git/dhowells/keyutils.git⟩
           on 2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2023-03-20.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    Linux                          15 Nov 2011                 REQUEST-KEY(8)

------------------------------------------------------------------------

Pages that refer to this page: [keyctl(1)](../man1/keyctl.1.html),  [keyctl(2)](../man2/keyctl.2.html),  [KEYCTL_ASSUME_AUTHORITY(2const)](../man2/KEYCTL_ASSUME_AUTHORITY.2const.html),  [KEYCTL_GET_KEYRING_ID(2const)](../man2/KEYCTL_GET_KEYRING_ID.2const.html),  [KEYCTL_INSTANTIATE(2const)](../man2/KEYCTL_INSTANTIATE.2const.html),  [request_key(2)](../man2/request_key.2.html),  [keyctl_instantiate(3)](../man3/keyctl_instantiate.3.html),  [keyctl_set_reqkey_keyring(3)](../man3/keyctl_set_reqkey_keyring.3.html),  [keyrings(7)](../man7/keyrings.7.html),  [keyutils(7)](../man7/keyutils.7.html),  [key.dns_resolver(8)](../man8/key.dns_resolver.8.html),  [nfsidmap(8)](../man8/nfsidmap.8.html)

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
