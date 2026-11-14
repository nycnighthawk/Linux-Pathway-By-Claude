---
{"title": "restorecon(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/restorecon.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# restorecon(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ARGUMENTS](#ARGUMENTS) \| [NOTES](#NOTES) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                          |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    restorecon(8)              SELinux User Command             restorecon(8)

## [](#NAME)NAME

           restorecon - restore file(s) default SELinux security contexts.

## [](#SYNOPSIS)SYNOPSIS

           restorecon [-r|-R] [-m] [-n] [-p] [-v] [-i] [-j] [-F] [-U] [-W]
           [-I|-D] [-x] [-e directory] pathname ...

           restorecon [-f infilename] [-e directory] [-r|-R] [-m] [-n] [-p]
           [-v] [-i] [-j] [-F] [-U] [-W] [-I|-D] [-x] [-T nthreads]

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the restorecon program.

           This program is primarily used to set the security context
           (extended attributes) on one or more files.

           It can also be run at any other time to correct inconsistent
           labels, to add support for newly-installed policy or, by using the
           -n option, to passively check whether the file contexts are all
           set as specified by the active policy (default behavior).

           If a file object does not have a context, restorecon will write
           the default context to the file object's extended attributes. If a
           file object has a context, restorecon will only modify the type
           portion of the security context.  The -F and -U options will force
           a replacement of the entire context.

           If a file is labeled with customizable SELinux type (for list of
           customizable types see
           /etc/selinux/{SELINUXTYPE}/contexts/customizable_types),
           restorecon won't reset the label unless the -F option is used.

           It is the same executable as setfiles but operates in a slightly
           different manner depending on its argv[0].

## [](#OPTIONS)OPTIONS

           -e directory
                  exclude a directory (repeat the option to exclude more than
                  one directory, Requires full path).

           -f infilename
                  infilename contains a list of files to be processed. Use
                  “-” for stdin.

           -j     skip files with multiple hard links to avoid unintentional
                  mislabeling, particularly when relabeling user-writable
                  directories.

           -F     Force reset of context to match file_context for
                  customizable files, and the default file context, changing
                  the user, role, range portion as well as the type.

           -U     In addition to the type portion also change the user and
                  role portions, but not the range portion.

           -h, -? display usage information and exit.

           -i     ignore files that do not exist.

           -I     ignore digest to force checking of labels even if the
                  stored SHA1 digest matches the specfiles SHA1 digest. The
                  digest will then be updated provided there are no errors.
                  See the NOTES section for further details.

           -D     Set or update any directory SHA1 digests. Use this option
                  to enable usage of the security.sehash extended attribute.

           -m     do not read /proc/mounts to obtain a list of non-seclabel
                  mounts to be excluded from relabeling checks.  Setting this
                  option is useful where there is a non-seclabel fs mounted
                  with a seclabel fs mounted on a directory below this.

           -n     don't change any file labels (passive check).  To display
                  the files whose labels would be changed, add -v.

           -o outfilename
                  Deprecated - This option is no longer supported.

           -p     show progress by printing the number of files in 1k blocks
                  unless relabeling the entire OS, that will then show the
                  approximate percentage complete. Note that the -p and -v
                  options are mutually exclusive.

           -R, -r change files and directories file labels recursively
                  (descend directories).  Directory cycles are skipped, see
                  the NOTES section for details.

           -v     show changes in file labels. Multiple -v options increase
                  the verbosity. Note that the -v and -p options are mutually
                  exclusive.

           -W     display warnings about entries that had no matching files
                  by outputting the selabel_stats(3) results.

           -c     count and display the number of (would be) relabeled files.
                  The exit code will be set to 0 only if at least one file is
                  relabeled.

           -0     the separator for the input items is assumed to be the null
                  character (instead of the white space).  The quotes and the
                  backslash characters are also treated as normal characters
                  that can form valid input.  This option finally also
                  disables the end of file string, which is treated like any
                  other argument.  Useful when input items might contain
                  white space, quote marks or backslashes.  The -print0
                  option of GNU find produces input suitable for this mode.

           -x     prevent restorecon from crossing file system boundaries.

           -T nthreads
                  use up to nthreads threads.  Specify 0 to create as many
                  threads as there are available CPU cores; 1 to use only a
                  single thread (default); or any positive number to use the
                  given number of threads (if possible).

## [](#ARGUMENTS)ARGUMENTS

                  pathname ...  The pathname for the file(s) to be relabeled.

## [](#NOTES)NOTES

           1.  restorecon by default does not operate recursively on
               directories. Paths leading up the final component of the
               file(s) are canonicalized using realpath(3) before labeling.

           2.  If the pathname specifies the root directory and the -vR or
               -vr options are set and the audit system is running, then an
               audit event is automatically logged stating that a "mass
               relabel" took place using the message label FS_RELABEL.

           3.  To improve performance when relabeling file systems
               recursively (i.e. the -R or -r option is set), the -D option
               to restorecon will cause it to store a SHA1 digest of the
               default specfiles set in an extended attribute named
               security.sehash on each directory specified in pathname ...
               once the relabeling has been completed successfully. These
               digests will be checked should restorecon -D be rerun with the
               same pathname parameters. See selinux_restorecon(3) for
               further details.

               The -I option will ignore the SHA1 digest from each directory
               specified in pathname ...  and provided the -n option is NOT
               set and recursive mode is set, files will be relabeled as
               required with the digests then being updated provided there
               are no errors.

           4.  When descending directories (i.e. the -R or -r option is set)
               restorecon detects directory cycles, for example a bind mount
               of an ancestor directory or nested BTRFS subvolumes. A cycle
               is reported as a warning and the offending directory is not
               descended into, the remaining entries are still relabeled.  A
               directory cycle is not counted as a relabeling error, so it
               does not affect the exit status and does not stop the file
               tree walk. Up to and including version 3.11 a directory cycle
               was instead treated as a fatal ELOOP error, terminating
               restorecon with a non-zero exit status.

## [](#EXAMPLE)EXAMPLE

           Fix labeling of /var/www/ including all sub-directories and list all context changes
           # restorecon -rv /var/www/
           List mislabeled files in user home directory and what the correct label should be
           # restorecon -nvr ~
           Fix labeling of files listed in file_list file, ignoring any that do not exist
           # restorecon -vif file_list

## [](#AUTHOR)AUTHOR

           This man page was written by Dan Walsh <dwalsh@redhat.com>.  Some
           of the content of this man page was taken from the setfiles man
           page written by Russell Coker <russell@coker.com.au>.  The program
           was written by Dan Walsh <dwalsh@redhat.com>.

## [](#SEE_ALSO)SEE ALSO

           setfiles(8), fixfiles(8), load_policy(8), checkpolicy(8),
           customizable_types(5)

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

                                   10 June 2016                 restorecon(8)

------------------------------------------------------------------------

Pages that refer to this page: [unsetfiles(1)](../man1/unsetfiles.1.html),  [selinux_restorecon_xattr(3)](../man3/selinux_restorecon_xattr.3.html),  [fixfiles(8)](../man8/fixfiles.8.html),  [restorecond(8)](../man8/restorecond.8.html),  [restorecon_xattr(8)](../man8/restorecon_xattr.8.html),  [selinux(8)](../man8/selinux.8.html),  [semanage-fcontext(8)](../man8/semanage-fcontext.8.html),  [setfiles(8)](../man8/setfiles.8.html)

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
