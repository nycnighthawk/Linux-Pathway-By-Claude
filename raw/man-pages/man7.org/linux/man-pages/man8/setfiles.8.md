---
{"title": "setfiles(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/setfiles.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# setfiles(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ARGUMENTS](#ARGUMENTS) \| [EXIT STATUS](#EXIT_STATUS) \| [NOTES](#NOTES) \| [EXAMPLE](#EXAMPLE) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    setfiles(8)                SELinux User Command               setfiles(8)

## [](#NAME)NAME

           setfiles - set SELinux file security contexts.

## [](#SYNOPSIS)SYNOPSIS

           setfiles [-c policy] [-C] [-d] [-j] [-l] [-m] [-n] [-e directory]
           [-E] [-p] [-s] [-v] [-W] [-F] [-U] [-I|-D] [-T nthreads] [-A]
           spec_file pathname ...

## [](#DESCRIPTION)DESCRIPTION

           This manual page describes the setfiles program.

           This program is primarily used to initialize the security context
           fields (extended attributes) on one or more filesystems (or parts
           of them).  Usually it is initially run as part of the SELinux
           installation process (a step commonly known as labeling).

           It can also be run at any other time to correct inconsistent
           labels, to add support for newly-installed policy or, by using the
           -n option, to passively check whether the file contexts are all
           set as specified by the active policy (default behavior) or by
           some other policy (see the -c option).

           If a file object does not have a context, setfiles will write the
           default context to the file object's extended attributes. If a
           file object has a context, setfiles will only modify the type
           portion of the security context.  The -U option will also modify
           the user and role portions of the security context.  The -F option
           will force a replacement of the entire context, including the
           range portion of the security context and modify customizable
           files.

## [](#OPTIONS)OPTIONS

           -c     check the validity of the contexts against the specified
                  binary policy.

           -C     If only relabeling errors are encountered during the file
                  tree walks, exit with status 1 rather than 255.

           -d     show what specification matched each file.

           -e directory
                  directory to exclude (repeat option for more than one
                  directory).

           -E     treat conflicting specifications as errors, such as where
                  two hardlinks for the same inode have different contexts.

           -f infilename
                  infilename contains a list of files to be processed. Use
                  “-” for stdin.

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

           -j     skip files with multiple hard links to avoid unintentional
                  mislabeling, particularly when relabeling user-writable
                  directories.

           -l     log changes in file labels to syslog.

           -m     do not read /proc/mounts to obtain a list of non-seclabel
                  mounts to be excluded from relabeling checks.  Setting this
                  option is useful where there is a non-seclabel fs mounted
                  with a seclabel fs mounted on a directory below this.

           -n     don't change any file labels (passive check).

           -o outfilename
                  Deprecated - This option is no longer supported.

           -p     show progress by printing the number of files in 1k blocks
                  unless relabeling the entire OS, that will then show the
                  approximate percentage complete. Note that the -p and -v
                  options are mutually exclusive.

           -q     Deprecated and replaced by -v. Has no effect on other
                  options or on program behavior.

           -r rootpath
                  use an alternate root path. Used in meta-selinux for
                  OpenEmbedded/Yocto builds to label files under rootpath as
                  if they were at /

           -s     take a list of files from standard input instead of using a
                  pathname from the command line (equivalent to “-f -” ).

           -v     show changes in file labels and output any inode
                  association parameters.  Note that the -v and -p options
                  are mutually exclusive.

           -W     display warnings about entries that had no matching files
                  by outputting the selabel_stats(3) results.

           -0     the separator for the input items is assumed to be the null
                  character (instead of the white space).  The quotes and the
                  backslash characters are also treated as normal characters
                  that can form valid input.  This option finally also
                  disables the end of file string, which is treated like any
                  other argument.  Useful when input items might contain
                  white space, quote marks or backslashes.  The -print0
                  option of GNU find produces input suitable for this mode.

           -T nthreads
                  use up to nthreads threads.  Specify 0 to create as many
                  threads as there are available CPU cores; 1 to use only a
                  single thread (default); or any positive number to use the
                  given number of threads (if possible).

           -A     do not track inodes with multiple hard links or bind mounts
                  that would match different contexts (saves memory)

## [](#ARGUMENTS)ARGUMENTS

           spec_file
                  The specification file which contains lines of the
                  following form:

                  regexp [type] context | <<none>>
                         The regular expression is anchored at both ends.
                         The optional type field specifies the file type as
                         shown in the mode field by the ls(1) program, e.g.
                         -- to match only regular files or -d to match only
                         directories.  The context can be an ordinary
                         security context or the string <<none>> to specify
                         that the file is not to have its context changed.
                         The last matching specification is used. If there
                         are multiple hard links to a file that match
                         different specifications and those specifications
                         indicate different security contexts, then a warning
                         is displayed but the file is still labeled based on
                         the last matching specification other than <<none>>.

           pathname ...
                  The pathname for the root directory of each file system to
                  be relabeled or a specific directory within a filesystem
                  that should be recursively descended and relabeled or the
                  pathname of a file that should be relabeled.  Not used if
                  the -f or the -s option is used.

## [](#EXIT_STATUS)EXIT STATUS

           setfiles exits with status 0 if it encounters no errors. Fatal
           errors result in status 255.  Labeling errors encountered during
           file tree walk(s) result in status 1 if the -C option is specified
           and no other kind of error is encountered, and in status 255
           otherwise.

## [](#NOTES)NOTES

           1.  setfiles operates recursively on directories. Paths leading up
               the final component of the file(s) are not canonicalized
               before labeling.

           2.  If the pathname specifies the root directory and the -v option
               is set and the audit system is running, then an audit event is
               automatically logged stating that a "mass relabel" took place
               using the message label FS_RELABEL.

           3.  To improve performance when relabeling file systems
               recursively the -D option to setfiles will cause it to store a
               SHA1 digest of the spec_file set in an extended attribute
               named security.sehash on each directory specified in
               pathname ...  once the relabeling has been completed
               successfully. These digests will be checked should setfiles -D
               be rerun with the same spec_file and pathname parameters. See
               selinux_restorecon(3) for further details.

               The -I option will ignore the SHA1 digest from each directory
               specified in pathname ...  and provided the -n option is NOT
               set, files will be relabeled as required with the digests then
               being updated provided there are no errors.

           4.  setfiles detects directory cycles while descending
               directories, for example a bind mount of an ancestor directory
               or nested BTRFS subvolumes. A cycle is reported as a warning
               and the offending directory is not descended into, the
               remaining entries are still relabeled. A directory cycle is
               not counted as a relabeling error, so it does not affect the
               exit status and does not stop the file tree walk. Up to and
               including version 3.11 a directory cycle was instead treated
               as a fatal ELOOP error, terminating setfiles with exit status
               255.

## [](#EXAMPLE)EXAMPLE

           Fix labeling of /var/www/ including all sub-directories, using targeted policy file context definitions and list all context changes
           # setfiles -v /etc/selinux/targeted/contexts/files/file_contexts /var/www/
           List mislabeled files in user home directory and what the label should be based on targeted policy file context definitions
           # setfiles -nv /etc/selinux/targeted/contexts/files/file_contexts ~
           Fix labeling of files listed in file_list file, ignoring any that do not exist
           # setfiles -vif file_list /etc/selinux/targeted/contexts/files/file_contexts

## [](#AUTHOR)AUTHOR

           This man page was written by Russell Coker <russell@coker.com.au>.
           The program was written by Stephen Smalley
           <stephen.smalley.work@gmail.com>

## [](#SEE_ALSO)SEE ALSO

           restorecon(8), load_policy(8), checkpolicy(8)

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

                                   10 June 2016                   setfiles(8)

------------------------------------------------------------------------

Pages that refer to this page: [unsetfiles(1)](../man1/unsetfiles.1.html),  [selinux_restorecon_xattr(3)](../man3/selinux_restorecon_xattr.3.html),  [customizable_types(5)](../man5/customizable_types.5.html),  [fixfiles(8)](../man8/fixfiles.8.html),  [restorecon(8)](../man8/restorecon.8.html),  [restorecon_xattr(8)](../man8/restorecon_xattr.8.html),  [selinux(8)](../man8/selinux.8.html)

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
