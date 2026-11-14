---
{"title": "git-index-pack(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-index-pack.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-index-pack(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [NOTES](#NOTES) \| [GIT](#GIT) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-INDEX-PACK(1)               Git Manual              GIT-INDEX-PACK(1)

## [](#NAME)NAME

           git-index-pack - Build pack index file for an existing packed
           archive

## [](#SYNOPSIS)SYNOPSIS

           git index-pack [-v] [-o <index-file>] [--[no-]rev-index] <pack-file>
           git index-pack --stdin [--fix-thin] [--keep] [-v] [-o <index-file>]
                             [--[no-]rev-index] [<pack-file>]

## [](#DESCRIPTION)DESCRIPTION

           Reads a packed archive (.pack) from the specified file, builds a
           pack index file (.idx) for it, and optionally writes a
           reverse-index (.rev) for the specified pack. The packed archive,
           together with the pack index, can then be placed in the
           objects/pack/ directory of a Git repository.

## [](#OPTIONS)OPTIONS

           -v
               Be verbose about what is going on, including progress status.

           -o <index-file>
               Write the generated pack index into the specified file.
               Without this option the name of pack index file is constructed
               from the name of packed archive file by replacing .pack with
               .idx (and the program fails if the name of packed archive does
               not end with .pack).

           --rev-index, --no-rev-index
               When this flag is provided, generate a reverse index (a .rev
               file) corresponding to the given pack. If --verify is given,
               ensure that the existing reverse index is correct. Takes
               precedence over pack.writeReverseIndex.

           --stdin
               When this flag is provided, the pack is read from stdin
               instead and a copy is then written to <pack-file>. If
               <pack-file> is not specified, the pack is written to
               objects/pack/ directory of the current Git repository with a
               default name determined from the pack content. If <pack-file>
               is not specified consider using --keep to prevent a race
               condition between this process and git repack.

           --fix-thin
               Fix a "thin" pack produced by git pack-objects --thin (see
               git-pack-objects(1) for details) by adding the excluded
               objects the deltified objects are based on to the pack. This
               option only makes sense in conjunction with --stdin.

           --keep
               Before moving the index into its final destination create an
               empty .keep file for the associated pack file. This option is
               usually necessary with --stdin to prevent a simultaneous git
               repack process from deleting the newly constructed pack and
               index before refs can be updated to use objects contained in
               the pack.

           --keep=<msg>
               Like --keep, create a .keep file before moving the index into
               its final destination. However, instead of creating an empty
               file place <msg> followed by an LF into the .keep file. The
               <msg> message can later be searched for within all .keep files
               to locate any which have outlived their usefulness.

           --index-version=<version>[,<offset>]
               This is intended to be used by the test suite only. It allows
               to force the version for the generated pack index, and to
               force 64-bit index entries on objects located above the given
               offset.

           --strict[=<msg-id>=<severity>...]
               Die, if the pack contains broken objects or links. An optional
               comma-separated list of <msg-id>=<severity> can be passed to
               change the severity of some possible issues, e.g.,
               --strict="missingEmail=ignore,badTagName=error". See the entry
               for the fsck.<msg-id> configuration options in git-fsck(1) for
               more information on the possible values of <msg-id> and
               <severity>.

           --progress-title
               For internal use only.

               Set the title of the progress bar. The title is "Receiving
               objects" by default and "Indexing objects" when --stdin is
               specified.

           --check-self-contained-and-connected
               Die if the pack contains broken links. For internal use only.

           --fsck-objects[=<msg-id>=<severity>...]
               Die if the pack contains broken objects, but unlike --strict,
               don’t choke on broken links. If the pack contains a tree
               pointing to a .gitmodules blob that does not exist, prints the
               hash of that blob (for the caller to check) after the hash
               that goes into the name of the pack/idx file (see "Notes").

               An optional comma-separated list of <msg-id>=<severity> can be
               passed to change the severity of some possible issues, e.g.,
               --fsck-objects="missingEmail=ignore,badTagName=ignore". See
               the entry for the fsck.<msg-id> configuration options in
               git-fsck(1) for more information on the possible values of
               <msg-id> and <severity>.

           --threads=<n>
               Specifies the number of threads to spawn when resolving
               deltas. This requires that index-pack be compiled with
               pthreads otherwise this option is ignored with a warning. This
               is meant to reduce packing time on multiprocessor machines.
               The required amount of memory for the delta search window is
               however multiplied by the number of threads. Specifying 0 will
               cause Git to auto-detect the number of CPU’s and use maximum 3
               threads.

           --max-input-size=<size>
               Die, if the pack is larger than <size>.

           --object-format=<hash-algorithm>
               Specify the given object format (hash algorithm) for the pack.
               The valid values are sha1 and (if enabled) sha256. The default
               is the algorithm for the current repository (set by
               extensions.objectFormat), or sha1 if no value is set or
               outside a repository.

               This option cannot be used with --stdin.

               Note: At present, there is no interoperability between SHA-256
               repositories and SHA-1 repositories.

           Historically, we warned that SHA-256 repositories may later need
           backward incompatible changes when we introduce such
           interoperability features. Today, we only expect compatible
           changes. Furthermore, if such changes prove to be necessary, it
           can be expected that SHA-256 repositories created with today’s Git
           will be usable by future versions of Git without data loss.

           --promisor[=<message>]
               Before committing the pack-index, create a .promisor file for
               this pack. Particularly helpful when writing a promisor pack
               with --fix-thin since the name of the pack is not final until
               the pack has been fully written. If a <message> is provided,
               then that content will be written to the .promisor file for
               future reference. See partial clone[1] for more information.

               Also, if there are objects in the given pack that references
               non-promisor objects (in the repo), repacks those non-promisor
               objects into a promisor pack. This avoids a situation in which
               a repo has non-promisor objects that are accessible through
               promisor objects.

               Requires <pack-file> to not be specified.

## [](#NOTES)NOTES

           Once the index has been created, the hash that goes into the name
           of the pack/idx file is printed to stdout. If --stdin was also
           used then this is prefixed by either "pack\t", or "keep\t" if a
           new .keep file was successfully created. This is useful to remove
           a .keep file used as a lock to prevent the race with git repack
           mentioned above.

## [](#GIT)GIT

           Part of the git(1) suite

## [](#NOTES)NOTES

            1. partial clone
               file:///home/mtk/share/doc/git-doc/technical/partial-clone.html

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

    Git 2.55.0.493.g5b2471          2026-08-03              GIT-INDEX-PACK(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-bundle(1)](../man1/git-bundle.1.html),  [git-config(1)](../man1/git-config.1.html),  [git-pack-objects(1)](../man1/git-pack-objects.1.html),  [git-show-index(1)](../man1/git-show-index.1.html)

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
