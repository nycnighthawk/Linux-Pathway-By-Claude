---
{"title": "fixfiles(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fixfiles.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fixfiles(8) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ARGUMENTS](#ARGUMENTS) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    fixfiles(8)                                                   fixfiles(8)

## [](#NAME)NAME

           fixfiles - fix file SELinux security contexts.

## [](#SYNOPSIS)SYNOPSIS

           fixfiles [-v] [-F] [-M] [-f] [-T nthreads] relabel

           fixfiles [-v] [-F] [-T nthreads] { check | restore | verify }
           dir/file ...

           fixfiles [-v] [-F] [-B | -N time ] [-T nthreads] { check | restore
           | verify }

           fixfiles [-v] [-F] [-T nthreads] -R
           rpmpackagename[,rpmpackagename...] { check | restore | verify }

           fixfiles [-v] [-F] [-T nthreads] -C PREVIOUS_FILECONTEXT { check |
           restore | verify }

           fixfiles [-F] [-M] [-B] [-T nthreads] onboot

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the fixfiles script.

           This  script  is  primarily  used  to correct the security context
           database (extended attributes) on filesystems.

           It can also be run at any time to relabel when adding support  for
           new  policy,  or   just check whether the file contexts are all as
           you expect.  By default it will relabel all  mounted  ext2,  ext3,
           ext4, gfs2, xfs, jfs and btrfs file systems as long as they do not
           have  a security context mount option.  You can use the -R flag to
           use    rpmpackages    as     an     alternative.      The     file
           /etc/selinux/fixfiles_exclude_dirs   can   contain   a   list   of
           directories excluded from relabeling.

           fixfiles onboot will setup the machine  to  relabel  on  the  next
           reboot.

## [](#OPTIONS)OPTIONS

           -B     If specified with onboot, this fixfiles will record the
                  current date in the /.autorelabel file, so that it can be
                  used later to speed up labeling. If used with restore, the
                  restore will only affect files that were modified today.

           -F     Force reset of context to match file_context for
                  customizable files

           -f     Clear /tmp directory with out prompt for removal.

           -R rpmpackagename[,rpmpackagename...]
                  Use the rpm database to discover all files within the
                  specified packages and restore the file contexts.

           -C PREVIOUS_FILECONTEXT
                  Run a diff on  the PREVIOUS_FILECONTEXT file to the
                  currently installed one, and restore the context of all
                  affected files.

           -N time
                  Only act on files created after the specified date.  Date
                  must be specified in "YYYY-MM-DD HH:MM" format.  Date field
                  will be passed to find --newermt command.

           -M     Bind mount filesystems before relabeling them, this allows
                  fixing the context of files or directories that have been
                  mounted over.

           -v     Modify verbosity from progress to verbose. (Run restorecon
                  with -v instead of -p)

           -T nthreads
                  Use parallel relabeling, see setfiles(8)

## [](#ARGUMENTS)ARGUMENTS

           One of:

           check | verify
                  print any incorrect file context labels, showing old and
                  new context, but do not change them.

           restore
                  change any incorrect file context labels.

           relabel
                  Prompt for removal of contents of /tmp directory and then
                  change any incorrect file context labels to match the
                  install file_contexts file.

           [[dir/file] ... ]
                  List of files or directories trees that you wish to check
                  file context on.

## [](#EXAMPLE)EXAMPLE

           Relabel the whole filesystem, except paths listed in /etc/selinux/fixfiles_exclude_dirs
           # fixfiles relabel
           Schedule the machine to relabel on the next boot and force relabeling of customizable types
           # fixfiles -F onboot
           Check labeling of all files from the samba package (while not changing any labels)
           # fixfiles -R samba check

## [](#AUTHOR)AUTHOR

           This man page was written by Richard Hally
           <rhally@mindspring.com>.  The script  was written by Dan Walsh
           <dwalsh@redhat.com>

## [](#SEE_ALSO)SEE ALSO

           setfiles(8), restorecon(8)

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

                                    2002031409                    fixfiles(8)

------------------------------------------------------------------------

Pages that refer to this page: [selinux_config(5)](../man5/selinux_config.5.html),  [restorecon(8)](../man8/restorecon.8.html),  [selinux(8)](../man8/selinux.8.html)

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
