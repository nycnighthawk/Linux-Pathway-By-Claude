---
{"title": "gitformat-loose(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/gitformat-loose.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gitformat-loose(5) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [LOOSE OBJECTS](#LOOSE_OBJECTS) \| [LOOSE OBJECT MAPPING](#LOOSE_OBJECT_MAPPING) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                   |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GITFORMAT-LOOSE(5)              Git Manual             GITFORMAT-LOOSE(5)

## [](#NAME)NAME

           gitformat-loose - Git loose object format

## [](#SYNOPSIS)SYNOPSIS

           $GIT_DIR/objects/[0-9a-f][0-9a-f]/*
           $GIT_DIR/objects/object-map/map-*.map

## [](#DESCRIPTION)DESCRIPTION

           Loose objects are how Git stores individual objects, where every
           object is written as a separate file.

           Over the lifetime of a repository, objects are usually written as
           loose objects initially. Eventually, these loose objects will be
           compacted into packfiles via repository maintenance to improve
           disk space usage and speed up the lookup of these objects.

## [](#LOOSE_OBJECTS)LOOSE OBJECTS

           Each loose object contains a prefix, followed immediately by the
           data of the object. The prefix contains <type> <size>\0. <type> is
           one of blob, tree, commit, or tag and size is the size of the data
           (without the prefix) as a decimal integer expressed in ASCII.

           The entire contents, prefix and data concatenated, is then
           compressed with zlib and the compressed data is stored in the
           file. The object ID of the object is the SHA-1 or SHA-256 (as
           appropriate) hash of the uncompressed data.

           The file for the loose object is stored under the objects
           directory, with the first two hex characters of the object ID
           being the directory and the remaining characters being the file
           name. This is done to shard the data and avoid too many files
           being in one directory, since some file systems perform poorly
           with many items in a directory.

           As an example, the empty tree contains the data (when
           uncompressed) tree 0\0 and, in a SHA-256 repository, would have
           the object ID
           6ef19b41225c5369f1c104d45d8d85efa9b057b53b14b4b9b939dd74decc5321
           and would be stored under
           $GIT_DIR/objects/6e/f19b41225c5369f1c104d45d8d85efa9b057b53b14b4b9b939dd74decc5321.

           Similarly, a blob containing the contents abc would have the
           uncompressed data of blob 3\0abc.

## [](#LOOSE_OBJECT_MAPPING)LOOSE OBJECT MAPPING

           When the compatObjectFormat option is used, Git needs to store a
           mapping between the repository’s main algorithm and the
           compatibility algorithm for loose objects as well as some
           auxiliary information.

           The mapping consists of a set of files under
           $GIT_DIR/objects/object-map ending in .map. The portion of the
           filename before the extension is that of the main hash checksum
           (that is, the one specified in extensions.objectformat) in hex
           format.

           git gc will repack existing entries into one file, removing any
           unnecessary objects, such as obsolete shallow entries or loose
           objects that have been packed.

           The file format is as follows. All values are in network byte
           order and all 4-byte and 8-byte values must be 4-byte aligned in
           the file, so the NUL padding may be required in some cases. Git
           always uses the smallest number of NUL bytes (including zero) that
           is required for the padding in order to make writing files
           deterministic.

           •   A header appears at the beginning and consists of the
               following:

               •   A 4-byte mapping signature: LMAP

               •   4-byte version number: 1

               •   4-byte length of the header section (including reserved
                   entries but excluding any NUL padding).

               •   4-byte number of objects declared in this map file.

               •   4-byte number of object formats declared in this map file.

               •   For each object format:

                   •   4-byte format identifier (e.g., sha1 for SHA-1)

                   •   4-byte length in bytes of shortened object names (that
                       is, prefixes of the full object names). This is the
                       shortest possible length needed to make names in the
                       shortened object name table unambiguous.

                   •   8-byte integer, recording where tables relating to
                       this format are stored in this index file, as an
                       offset from the beginning.

               •   8-byte offset to the trailer from the beginning of this
                   file.

               •   The remainder of the header section is reserved for future
                   use. Readers must ignore unrecognized data here.

           •   Zero or more NUL bytes. These are used to improve the
               alignment of the 4-byte quantities below.

           •   Tables for the first object format:

               •   A sorted table of shortened object names. These are
                   prefixes of the names of all objects in this file, packed
                   together to reduce the cache footprint of the binary
                   search for a specific object name.

               •   A sorted table of full object names.

               •   A table of 4-byte metadata values.

           •   Zero or more NUL bytes.

           •   Tables for subsequent object formats:

               •   A sorted table of shortened object names. These are
                   prefixes of the names of all objects in this file, packed
                   together without offset values to reduce the cache
                   footprint of the binary search for a specific object name.

               •   A table of full object names in the order specified by the
                   first object format.

               •   A table of 4-byte values mapping object name order to the
                   order of the first object format. For an object in the
                   table of sorted shortened object names, the value at the
                   corresponding index in this table is the index in the
                   previous table for that same object.

               •   Zero or more NUL bytes.

           •   The trailer consists of the following:

               •   Hash checksum of all of the above using the main hash.

           The lower six bits of each metadata table contain a type field
           indicating the reason that this object is stored:

           0
               Reserved.

           1
               This object is stored as a loose object in the repository.

           2
               This object is a shallow entry. The mapping refers to a
               shallow value returned by a remote server.

           3
               This object is a submodule entry. The mapping refers to the
               commit stored representing a submodule.

           Other data may be stored in this field in the future. Bits that
           are not used must be zero.

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

    Git 2.55.0.493.g5b2471          2026-08-03             GITFORMAT-LOOSE(5)

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
