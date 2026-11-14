---
{"title": "git-hash-object(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-hash-object.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-hash-object(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-HASH-OBJECT(1)              Git Manual             GIT-HASH-OBJECT(1)

## [](#NAME)NAME

           git-hash-object - Compute object ID and optionally create an
           object from a file

## [](#SYNOPSIS)SYNOPSIS

           git hash-object [-t <type>] [-w] [--path=<file> | --no-filters]
                           [--stdin [--literally]] [--] <file>...
           git hash-object [-t <type>] [-w] --stdin-paths [--no-filters]

## [](#DESCRIPTION)DESCRIPTION

           Computes the object ID value for an object with specified type
           with the contents of the named file (which can be outside of the
           work tree), and optionally writes the resulting object into the
           object database. Reports its object ID to its standard output.
           When <type> is not specified, it defaults to "blob".

## [](#OPTIONS)OPTIONS

           -t <type>
               Specify the type of object to be created (default: "blob").
               Possible values are commit, tree, blob, and tag.

           -w
               Actually write the object into the object database.

           --stdin
               Read the object from standard input instead of from a file.

           --stdin-paths
               Read file names from the standard input, one per line, instead
               of from the command-line.

           --path
               Hash object as if it were located at the given path. The
               location of the file does not directly influence the hash
               value, but the path is used to determine which Git filters
               should be applied to the object before it can be placed in the
               object database. As a result of applying filters, the actual
               blob put into the object database may differ from the given
               file. This option is mainly useful for hashing temporary files
               located outside of the working directory or files read from
               stdin.

           --no-filters
               Hash the contents as is, ignoring any input filter that would
               have been chosen by the attributes mechanism, including the
               end-of-line conversion. If the file is read from standard
               input then this is always implied, unless the --path option is
               given.

           --literally
               Allow --stdin to hash any garbage into a loose object which
               might not otherwise pass standard object parsing or git-fsck
               checks. Useful for stress-testing Git itself or reproducing
               characteristics of corrupt or bogus objects encountered in the
               wild.

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

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-HASH-OBJECT(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-merge-tree(1)](../man1/git-merge-tree.1.html),  [git-mktag(1)](../man1/git-mktag.1.html),  [git-replace(1)](../man1/git-replace.1.html)

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
