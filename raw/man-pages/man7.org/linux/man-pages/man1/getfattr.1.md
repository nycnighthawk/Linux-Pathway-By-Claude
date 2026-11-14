---
{"title": "getfattr(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/getfattr.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# getfattr(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [AUTHOR](#AUTHOR) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GETFATTR(1)                   File Utilities                  GETFATTR(1)

## [](#NAME)NAME

           getfattr - get extended attributes of filesystem objects

## [](#SYNOPSIS)SYNOPSIS

           getfattr [-hRLP] -n name [-e en] pathname...
           getfattr [-hRLP] -d [-e en] [-m pattern] pathname...

## [](#DESCRIPTION)DESCRIPTION

           For each file, getfattr displays the file name, and the set of
           extended attribute names (and optionally values) which are
           associated with that file. Per default only attributes in the user
           namespace are displayed, see -m.

           The output format of getfattr -d is as follows:
                   1:  # file: somedir/
                   2:  user.name0="value0"
                   3:  user.name1="value1"
                   4:  user.name2="value2"
                   5:  ...

           Line 1 identifies the file name for which the following lines are
           being reported.  The remaining lines (lines 2 to 4 above) show the
           name and value pairs associated with the specified file.

## [](#OPTIONS)OPTIONS

           -n name, --name=name
               Dump the value of the named extended attribute.

           -d, --dump
               Dump the values of all matched extended attributes.

           -e en, --encoding=en
               Encode values after retrieving them.  Valid values of en are
               "text", "hex", and "base64".  Values encoded as text strings
               are enclosed in double quotes ("), while strings encoded as
               hexadecimal and base64 are prefixed with 0x and 0s,
               respectively.

           -h, --no-dereference
               Do not dereference symlinks. Instead of the file a symlink
               refers to, the symlink itself is examined.

           -m pattern, --match=pattern
               Only include attributes with names matching the regular
               expression pattern.  The default value for pattern is
               "^user\\.", which includes all the attributes in the user
               namespace. Specify "-" for including all attributes.  Refer to
               xattr(7) for a more detailed discussion of namespaces.

           --absolute-names
               Do not strip leading slash characters ('/').  The default
               behaviour is to strip leading slash characters.

           --only-values
               Dump out the raw extended attribute value(s) without encoding
               them.

           -R, --recursive
               List the attributes of all files and directories recursively.
               This option is commonly used together with option -h.

           -L, --logical
               Logical walk, recurse into symbolic links that refer to a
               directory.  Only effective in combination with -R.  The
               default behaviour is to recurse into symbolic links given on
               the command line, and not to recurse into symbolic links
               encountered in subdirectories.

           -P, --physical
               Physical walk, do not recurse into symbolic links that refer
               to a directory.  Only effective in combination with -R.  (For
               pathnames given on the command line, this option applies only
               to the final component; preceding path components may still be
               symbolic links.)

           --version
               Print the version of getfattr and exit.

           --help
               Print help explaining the command line options.

           --  End of command line options.  All remaining parameters are
               interpreted as file names, even if they start with a dash
               character.

## [](#AUTHOR)AUTHOR

           Andreas Gruenbacher, <andreas.gruenbacher@gmail.com> and the SGI
           XFS development team, <linux-xfs@oss.sgi.com>.

           Please send your bug reports or comments to
           <https://savannah.nongnu.org/bugs/?group=attr > or <acl-
           devel@nongnu.org>.

## [](#SEE_ALSO)SEE ALSO

           setfattr(1), xattr(7)

## [](#COLOPHON)COLOPHON

           This page is part of the attr (manipulating filesystem extended
           attributes) project.  Information about the project can be found
           at ⟨http://savannah.nongnu.org/projects/attr⟩.  If you have a bug
           report for this manual page, see
           ⟨http://savannah.nongnu.org/bugs/?group=attr⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.savannah.nongnu.org/attr.git⟩ on 2026-08-03.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-06-29.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Dec 2001                   Extended Attributes                GETFATTR(1)

------------------------------------------------------------------------

Pages that refer to this page: [attr(1)](../man1/attr.1.html),  [setfattr(1)](../man1/setfattr.1.html),  [getxattr(2)](../man2/getxattr.2.html),  [listxattr(2)](../man2/listxattr.2.html),  [removexattr(2)](../man2/removexattr.2.html),  [setxattr(2)](../man2/setxattr.2.html),  [selinux_restorecon(3)](../man3/selinux_restorecon.3.html),  [tmpfiles.d(5)](../man5/tmpfiles.d.5.html),  [xattr(7)](../man7/xattr.7.html),  [systemd-coredump(8)](../man8/systemd-coredump.8.html)

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
