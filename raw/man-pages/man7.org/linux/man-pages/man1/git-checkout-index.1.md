---
{"title": "git-checkout-index(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-checkout-index.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-checkout-index(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [USING \--TEMP OR \--STAGE=ALL](#USING_--TEMP_OR_--STAGE=ALL) \| [EXAMPLES](#EXAMPLES) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-CHECKOUT-INDEX(1)           Git Manual          GIT-CHECKOUT-INDEX(1)

## [](#NAME)NAME

           git-checkout-index - Copy files from the index to the working tree

## [](#SYNOPSIS)SYNOPSIS

           git checkout-index [-u] [-q] [-a] [-f] [-n] [--prefix=<string>]
                              [--stage=<number>|all]
                              [--temp]
                              [--ignore-skip-worktree-bits]
                              [-z] [--stdin]
                              [--] [<file>...]

## [](#DESCRIPTION)DESCRIPTION

           Copies all listed files from the index to the working directory
           (not overwriting existing files).

## [](#OPTIONS)OPTIONS

           -u, --index
               update stat information for the checked out entries in the
               index file.

           -q, --quiet
               be quiet if files exist or are not in the index

           -f, --force
               forces overwrite of existing files

           -a, --all
               checks out all files in the index except for those with the
               skip-worktree bit set (see --ignore-skip-worktree-bits).
               Cannot be used together with explicit filenames.

           -n, --no-create
               Don’t checkout new files, only refresh files already checked
               out.

           --prefix=<string>
               When creating files, prepend <string> (usually a directory
               including a trailing /)

           --stage=<number>|all
               Instead of checking out unmerged entries, copy out the files
               from the named stage. <number> must be between 1 and 3. Note:
               --stage=all automatically implies --temp.

           --temp
               Instead of copying the files to the working directory, write
               the content to temporary files. The temporary name
               associations will be written to stdout.

           --ignore-skip-worktree-bits
               Check out all files, including those with the skip-worktree
               bit set.

           --stdin
               Instead of taking a list of paths from the command line, read
               the list of paths from the standard input. Paths are separated
               by LF (i.e. one path per line) by default.

           -z
               Only meaningful with --stdin; paths are separated with NUL
               character instead of LF.

           --
               Do not interpret any more arguments as options.

           The order of the flags used to matter, but not anymore.

           Just doing git checkout-index does nothing. You probably meant git
           checkout-index -a. And if you want to force it, you want git
           checkout-index -f -a.

           Intuitiveness is not the goal here. Repeatability is. The reason
           for the "no arguments means no work" behavior is that from scripts
           you are supposed to be able to do:

               $ find . -name '*.h' -print0 | xargs -0 git checkout-index -f --

           which will force all existing *.h files to be replaced with their
           cached copies. If an empty command line implied "all", then this
           would force-refresh everything in the index, which was not the
           point. But since git checkout-index accepts --stdin it would be
           faster to use:

               $ find . -name '*.h' -print0 | git checkout-index -f -z --stdin

           The -- is just a good idea when you know the rest will be
           filenames; it will prevent problems with a filename of, for
           example, -a. Using -- is probably a good policy in scripts.

## [](#USING_--TEMP_OR_--STAGE=ALL)USING \--TEMP OR \--STAGE=ALL

           When --temp is used (or implied by --stage=all) git checkout-index
           will create a temporary file for each index entry being checked
           out. The index will not be updated with stat information. These
           options can be useful if the caller needs all stages of all
           unmerged entries so that the unmerged files can be processed by an
           external merge tool.

           A listing will be written to stdout providing the association of
           temporary file names to tracked path names. The listing format has
           two variations:

            1. tempname TAB path RS

               The first format is what gets used when --stage is omitted or
               is not --stage=all. The field tempname is the temporary file
               name holding the file content and path is the tracked path
               name in the index. Only the requested entries are output.

            2. stage1temp SP stage2temp SP stage3tmp TAB path RS

               The second format is what gets used when --stage=all. The
               three stage temporary fields (stage1temp, stage2temp,
               stage3temp) list the name of the temporary file if there is a
               stage entry in the index or . if there is no stage entry.
               Paths which only have a stage 0 entry will always be omitted
               from the output.

           In both formats RS (the record separator) is newline by default
           but will be the null byte if -z was passed on the command line.
           The temporary file names are always safe strings; they will never
           contain directory separators or whitespace characters. The path
           field is always relative to the current directory and the
           temporary file names are always relative to the top level
           directory.

           If the object being copied out to a temporary file is a symbolic
           link the content of the link will be written to a normal file. It
           is up to the end-user or the Porcelain to make use of this
           information.

## [](#EXAMPLES)EXAMPLES

           To update and refresh only the files already checked out

                   $ git checkout-index -n -f -a && git update-index --ignore-missing --refresh

           Using git checkout-index to "export an entire tree"
               The prefix ability basically makes it trivial to use git
               checkout-index as an "export as tree" function. Just read the
               desired tree into the index, and do:

                   $ git checkout-index --prefix=git-export-dir/ -a

               git checkout-index will "export" the index into the specified
               directory.

               The final "/" is important. The exported name is literally
               just prefixed with the specified string. Contrast this with
               the following example.

           Export files with a prefix

                   $ git checkout-index --prefix=.merged- Makefile

               This will check out the currently cached copy of Makefile into
               the file .merged-Makefile.

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

    Git 2.55.0.493.g5b2471          2026-08-03          GIT-CHECKOUT-INDEX(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-read-tree(1)](../man1/git-read-tree.1.html)

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
