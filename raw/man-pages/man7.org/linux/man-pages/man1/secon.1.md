---
{"title": "secon(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/secon.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# secon(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SECON(1)                 General Commands Manual                 SECON(1)

## [](#NAME)NAME

           secon - See an SELinux context, from a file, program or user
           input.

## [](#SYNOPSIS)SYNOPSIS

           secon [-hVurtscmPRfLp] [CONTEXT]
           [--file] FILE
           [--link] FILE
           [--pid] PID

## [](#DESCRIPTION)DESCRIPTION

           See a part of a context. The context is taken from a file, pid,
           user input or the context in which secon is originally executed.

           -V, --version
                  shows the current version of secon

           -h, --help
                  shows the usage information for secon

           -P, --prompt
                  outputs data in a format suitable for a prompt

           -C, --color
                  outputs data with the associated ANSI color codes (requires
                  -P)

           -u, --user
                  show the user of the security context

           -r, --role
                  show the role of the security context

           -t, --type
                  show the type of the security context

           -s, --sensitivity
                  show the sensitivity level of the security context

           -c, --clearance
                  show the clearance level of the security context

           -m, --mls-range
                  show the sensitivity level and clearance, as a range, of
                  the security context

           -R, --raw
                  outputs  the sensitivity level and clearance in an
                  untranslated format.

           -f, --file
                  gets the context from the specified file FILE

           -L, --link
                  gets the context from the specified file FILE (doesn't
                  follow symlinks)

           -p, --pid
                  gets the context from the specified process PID

           --pid-exec
                  gets the exec context from the specified process PID

           --pid-fs
                  gets the fscreate context from the specified process PID

           --pid-key
                  gets the key context from the specified process PID

           --current, --self
                  gets the context from the current process

           --current-exec, --self-exec
                  gets the exec context from the current process

           --current-fs, --self-fs
                  gets the fscreate context from the current process

           --current-key, --self-key
                  gets the key context from the current process

           --parent
                  gets the context from the parent of the current process

           --parent-exec
                  gets the exec context from the parent of the current
                  process

           --parent-fs
                  gets the fscreate context from the parent of the current
                  process

           --parent-key
                  gets the key context from the parent of the current process

           Additional argument CONTEXT may be provided and will be used if no
           options have been specified to make secon get its context from
           another source.  If that argument is - then the context will be
           read from stdin.
           If there is no argument, secon will try reading a context from
           stdin, if that is not a tty, otherwise secon will act as though
           --self had been passed.

           If none of --user, --role, --type, --level or --mls-range is
           passed.  Then all of them will be output.

## [](#EXAMPLE)EXAMPLE

           Show SElinux context of the init process
           # secon --pid 1
           Parse the type portion of given security context
           # secon -t system_u:object_r:httpd_sys_rw_content_t:s0

## [](#SEE_ALSO)SEE ALSO

           chcon(1)

## [](#AUTHORS)AUTHORS

           James Antill (james.antill@redhat.com)

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

    Security Enhanced Linux         April 2006                       SECON(1)

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
