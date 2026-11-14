---
{"title": "semanage-fcontext(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/semanage-fcontext.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# semanage-fcontext(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLE](#EXAMPLE) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                            |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    semanage-fcontext(8)                                 semanage-fcontext(8)

## [](#NAME)NAME

           semanage-fcontext - SELinux Policy Management file context tool

## [](#SYNOPSIS)SYNOPSIS

           semanage fcontext [-h] [-n] [-N] [-S STORE] [ --add ( -t TYPE -f
           FTYPE -r RANGE -s SEUSER | -e TARGET_PATH ) FILE_SPEC | --delete (
           -t TYPE -f FTYPE | -e TARGET_PATH ) FILE_SPEC | --deleteall |
           --extract | --list [-C] | --modify ( -t TYPE -f FTYPE -r RANGE -s
           SEUSER | -e TARGET_PATH ) FILE_SPEC ]

## [](#DESCRIPTION)DESCRIPTION

           semanage is used to configure certain elements of SELinux policy
           without requiring modification to or recompilation from policy
           sources.  semanage fcontext is used to manage the default file
           system labeling on an SELinux system.  This command maps file
           paths using regular expressions to SELinux labels.

           FILE_SPEC may contain either a fully qualified path, or a Perl
           compatible regular expression (PCRE), describing fully qualified
           path(s). The only PCRE flag in use is PCRE2_DOTALL, which causes a
           wildcard '.' to match anything, including a new line.  Strings
           representing paths are processed as bytes (as opposed to Unicode),
           meaning that non-ASCII characters are not matched by a single
           wildcard.

           Note, that file context definitions specified using 'semanage
           fcontext' (i.e. local file context modifications stored in
           file_contexts.local) have higher priority than those specified in
           policy modules.  This means that whenever a match for given file
           path is found in file_contexts.local, no other file context
           definitions are considered.  Entries in file_contexts.local are
           processed from most recent one to the oldest, with first match
           being used (as opposed to the most specific match, which is used
           when matching other file context definitions).  All regular
           expressions should therefore be as specific as possible, to avoid
           unintentionally impacting other parts of the filesystem.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Show this help message and exit

           -n, --noheading
                  Do not print heading when listing the specified object type

           -N, --noreload
                  Do not reload policy after commit

           -C, --locallist
                  List local customizations

           -S STORE, --store STORE
                  Select an alternate SELinux Policy Store to manage

           -a, --add
                  Add a record of the specified object type

           -d, --delete
                  Delete a record of the specified object type

           -m, --modify
                  Modify a record of the specified object type

           -l, --list
                  List records of the specified object type

           -E, --extract
                  Extract customizable commands, for use within a transaction

           -D, --deleteall
                  Remove all local customizations

           -e TARGET_PATH, --equal TARGET_PATH
                  Substitute FILE_SPEC with TARGET_PATH for file label
                  lookup. This is used with fcontext. Requires source and
                  target path arguments to be path prefixes and does not
                  support regular expressions. The context labeling for the
                  target subtree is made equivalent to that defined for the
                  source. Note that substitution based on another
                  substitution does not work.

           -f [{a,f,d,c,b,s,l,p}], --ftype [{a,f,d,c,b,s,l,p}]
                  File Type. This is used with fcontext. Requires a file type
                  as shown in the mode field by ls, e.g. use 'd' to match
                  only directories or 'f' to match only regular files. The
                  following file type options can be passed: f (regular
                  file),d (directory),c (character device), b (block
                  device),s (socket),l (symbolic link),p (named pipe).  If
                  you do not specify a file type, the file type will default
                  to "all files".

           -s SEUSER, --seuser SEUSER
                  SELinux user name

           -t TYPE, --type TYPE
                  SELinux Type for the object

           -r RANGE, --range RANGE
                  MLS/MCS Security Range (MLS/MCS Systems only) SELinux Range
                  for SELinux login mapping defaults to the SELinux user
                  record range. SELinux Range for SELinux user defaults to
                  s0.

## [](#EXAMPLE)EXAMPLE

           Remember to run restorecon after you set the file context
           Add file-context httpd_sys_content_t for everything under /web
           # semanage fcontext -a -t httpd_sys_content_t "/web(/.*)?"
           # restorecon -R -v /web

           Substitute /home1 with /home when setting file context
           i.e. label everything under /home1 the same way /home is labeled
           # semanage fcontext -a -e /home /home1
           # restorecon -R -v /home1

           If you substitute /home2 with /home1 from the example above it will not work. You must use direct substitution
           # semanage fcontext -a -e /home /home2
           # restorecon -R -v /home2

           For home directories under top level directory, for example /disk6/home,
           execute the following commands.
           # semanage fcontext -a -t home_root_t "/disk6"
           # semanage fcontext -a -e /home /disk6/home
           # restorecon -R -v /disk6

           Add file-context with MLS range s0:c0.c255 for /secure directory (MLS/MCS systems only)
           # semanage fcontext -a -t admin_home_t -r s0:c0.c255 "/secure(/.*)?"
           # restorecon -R -F -v /secure

## [](#SEE_ALSO)SEE ALSO

           selinux(8), semanage(8), restorecon(8), selabel_file(5)

## [](#AUTHOR)AUTHOR

           This man page was written by Daniel Walsh <dwalsh@redhat.com>

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

                                     20130617            semanage-fcontext(8)

------------------------------------------------------------------------

Pages that refer to this page: [semanage(8)](../man8/semanage.8.html)

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
