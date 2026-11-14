---
{"title": "git-repo(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-repo.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-repo(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [INFO KEYS](#INFO_KEYS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-REPO(1)                     Git Manual                    GIT-REPO(1)

## [](#NAME)NAME

           git-repo - Retrieve information about the repository

## [](#SYNOPSIS)SYNOPSIS

           git repo info [--format=(lines|nul) | -z] [--all | <key>...]
           git repo info --keys [--format=(lines|nul) | -z]
           git repo structure [--format=(table|lines|nul) | -z]

## [](#DESCRIPTION)DESCRIPTION

           Retrieve information about the repository.

           THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.

## [](#COMMANDS)COMMANDS

           info [--format=(lines|nul) | -z] [--all | <key>...]
               Retrieve metadata-related information about the current
               repository. Only the requested data will be returned based on
               their keys (see "INFO KEYS" section below).

               The values are returned in the same order in which their
               respective keys were requested. The --all flag requests the
               values for all the available keys.

               The output format can be chosen through the flag --format. Two
               formats are supported:

               lines
                   Output key-value pairs one per line using the = character
                   as the delimiter between the key and the value. Values
                   containing "unusual" characters are quoted as explained
                   for the configuration variable core.quotePath (see
                   git-config(1)). This is the default.

               nul
                   Similar to lines, but using a newline character as the
                   delimiter between the key and the value and using a NUL
                   character after each value. This format is better suited
                   for being parsed by another applications than lines.
                   Unlike in the lines format, the values are never quoted.

                   -z is an alias for --format=nul.

           info --keys [--format=(lines|nul) | -z]
               List all the available keys, one per line. The output format
               can be chosen through the flag --format. The following formats
               are supported:

               lines
                   Output the keys one per line. This is the default.

               nul
                   Similar to lines, but using a NUL character after each
                   value.

           structure [--format=(table|lines|nul) | -z]
               Retrieve statistics about the current repository structure.
               The following kinds of information are reported:

               •   Reference counts categorized by type

               •   Reachable object counts categorized by type

               •   Total inflated size of reachable objects by type

               •   Total disk size of reachable objects by type

               •   Largest reachable objects in the repository by type

                   The output format can be chosen through the flag --format.
                   Three formats are supported:

                   table
                       Outputs repository stats in a human-friendly table.
                       This format may change and is not intended for machine
                       parsing. This is the default format.

                   lines
                       Each line of output contains a key-value pair for a
                       repository stat. The = character is used to delimit
                       between the key and the value. Values containing
                       "unusual" characters are quoted as explained for the
                       configuration variable core.quotePath (see
                       git-config(1)).

                   nul
                       Similar to lines, but uses a NUL character to delimit
                       between key-value pairs instead of a newline. Also
                       uses a newline character as the delimiter between the
                       key and value instead of =. Unlike the lines format,
                       values containing "unusual" characters are never
                       quoted.

                       -z is an alias for --format=nul.

## [](#INFO_KEYS)INFO KEYS

           In order to obtain a set of values from git repo info, you should
           provide the keys that identify them. Here’s a list of the
           available keys and the values that they return:

           layout.bare
               true if this is a bare repository, otherwise false.

           layout.shallow
               true if this is a shallow repository, otherwise false.

           object.format
               The object format (hash algorithm) used in the repository.

           path.commondir.absolute
               The canonical absolute path to the Git repository’s common
               directory (the shared .git directory containing objects, refs,
               and global configuration).

           path.commondir.relative
               The path to the Git repository’s common directory relative to
               the current working directory.

           path.gitdir.absolute
               The canonical absolute path to the Git repository directory
               (the .git directory).

           path.gitdir.relative
               The path to the Git repository directory relative to the
               current working directory.

           references.format
               The reference storage format. The valid values are:

               files
                   for loose files with packed-refs. This is the default.

               reftable
                   for the reftable format.

## [](#EXAMPLES)EXAMPLES

           •   Retrieves the reference format of the current repository:

                   git repo info references.format

           •   Retrieves whether the current repository is bare and whether
               it is shallow using the nul format:

                   git repo info --format=nul layout.bare layout.shallow

## [](#SEE_ALSO)SEE ALSO

           git-rev-parse(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03                    GIT-REPO(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html)

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
