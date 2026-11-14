---
{"title": "matchpathcon(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/matchpathcon.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# matchpathcon(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    matchpathcon(8)     SELinux Command Line documentation    matchpathcon(8)

## [](#NAME)NAME

           matchpathcon - get the default SELinux security context for the
           specified path from the file contexts configuration

## [](#SYNOPSIS)SYNOPSIS

           matchpathcon [-V] [-N] [-n] [-m type] [-f file_contexts_file] [-p
           prefix] [-P policy_root_path] filepath...

## [](#DESCRIPTION)DESCRIPTION

           matchpathcon queries the system policy and outputs the default
           security context associated with the filepath.

           Note: Identical paths can have different security contexts,
           depending on the file type (regular file, directory, link file,
           char file ...).

           matchpathcon will also take the file type into consideration in
           determining the default security context if the file exists. If
           the file does not exist, no file type matching will occur.

## [](#OPTIONS)OPTIONS

           -m type
                  Force file type for the lookup.  Valid types are file, dir,
                  pipe, chr_file, blk_file, lnk_file, sock_file

           -n     Do not display path

           -N     Do not use translations

           -f file_context_file
                  Use alternate file_context file

           -p prefix
                  Use prefix to speed up translations

           -P policy_root_path
                  Use alternate policy root path

           -V     Verify file context on disk matches defaults

## [](#EXAMPLE)EXAMPLE

           Show the default label of sock_file cups.sock
           # matchpathcon -m sock_file /var/run/cups/cups.sock
           Verify that /var/www/html directory is labeled correctly (the content of the folder is not checked)
           # matchpathcon -V /var/www/html

## [](#AUTHOR)AUTHOR

           This manual page was written by Dan Walsh <dwalsh@redhat.com>.

## [](#SEE_ALSO)SEE ALSO

           selinux(8), matchpathcon(3)

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    dwalsh@redhat.com             21 April 2005               matchpathcon(8)

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
