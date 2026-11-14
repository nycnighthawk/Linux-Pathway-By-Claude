---
{"title": "git-check-attr(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-check-attr.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-check-attr(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-CHECK-ATTR(1)               Git Manual              GIT-CHECK-ATTR(1)

## [](#NAME)NAME

           git-check-attr - Display gitattributes information

## [](#SYNOPSIS)SYNOPSIS

           git check-attr [--source <tree-ish>] [-a | --all | <attr>...] [--] <pathname>...
           git check-attr --stdin [-z] [--source <tree-ish>] [-a | --all | <attr>...]

## [](#DESCRIPTION)DESCRIPTION

           For every pathname, this command will list if each attribute is
           unspecified, set, or unset as a gitattribute on that pathname.

## [](#OPTIONS)OPTIONS

           -a, --all
               List all attributes that are associated with the specified
               paths. If this option is used, then unspecified attributes
               will not be included in the output.

           --cached
               Consider .gitattributes in the index only, ignoring the
               working tree.

           --stdin
               Read pathnames from the standard input, one per line, instead
               of from the command line.

           -z
               The output format is modified to be machine-parsable. If
               --stdin is also given, input paths are separated with a NUL
               character instead of a linefeed character.

           --source=<tree-ish>
               Check attributes against the specified tree-ish. It is common
               to specify the source tree by naming a commit, branch, or tag
               associated with it.

           --
               Interpret all preceding arguments as attributes and all
               following arguments as path names.

           If none of --stdin, --all, or -- is used, the first argument will
           be treated as an attribute and the rest of the arguments as
           pathnames.

## [](#OUTPUT)OUTPUT

           The output is of the form: <path> COLON SP <attribute> COLON SP
           <info> LF

           unless -z is in effect, in which case NUL is used as delimiter:
           <path> NUL <attribute> NUL <info> NUL

           <path> is the path of a file being queried, <attribute> is an
           attribute being queried, and <info> can be either:

           unspecified
               when the attribute is not defined for the path.

           unset
               when the attribute is defined as false.

           set
               when the attribute is defined as true.

           <value>
               when a value has been assigned to the attribute.

           Buffering happens as documented under the GIT_FLUSH option in
           git(1). The caller is responsible for avoiding deadlocks caused by
           overfilling an input buffer or reading from an empty output
           buffer.

## [](#EXAMPLES)EXAMPLES

           In the examples, the following .gitattributes file is used:

               *.java diff=java -crlf myAttr
               NoMyAttr.java !myAttr
               README caveat=unspecified

           •   Listing a single attribute:

                   $ git check-attr diff org/example/MyClass.java
                   org/example/MyClass.java: diff: java

           •   Listing multiple attributes for a file:

                   $ git check-attr crlf diff myAttr -- org/example/MyClass.java
                   org/example/MyClass.java: crlf: unset
                   org/example/MyClass.java: diff: java
                   org/example/MyClass.java: myAttr: set

           •   Listing all attributes for a file:

                   $ git check-attr --all -- org/example/MyClass.java
                   org/example/MyClass.java: diff: java
                   org/example/MyClass.java: myAttr: set

           •   Listing an attribute for multiple files:

                   $ git check-attr myAttr -- org/example/MyClass.java org/example/NoMyAttr.java
                   org/example/MyClass.java: myAttr: set
                   org/example/NoMyAttr.java: myAttr: unspecified

           •   Not all values are equally unambiguous:

                   $ git check-attr caveat README
                   README: caveat: unspecified

## [](#SEE_ALSO)SEE ALSO

           gitattributes(5).

## [](#GIT)GIT

           Part of the git(1) suite

## [](#COLOPHON)COLOPHON

           This page is part of the git (Git distributed version control
           system) project.  Information about the project can be found at 
           ⟨http://git-scm.com/⟩.  If you have a bug report for this manual
           page, see ⟨http://git-scm.com/community⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://github.com/git/git.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    Git 2.55.0.493.g5b2471          2026-08-03              GIT-CHECK-ATTR(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [gitattributes(5)](../man5/gitattributes.5.html)

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
