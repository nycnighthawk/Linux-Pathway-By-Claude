---
{"title": "git-refs(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-refs.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-refs(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COMMANDS](#COMMANDS) \| [OPTIONS](#OPTIONS) \| [KNOWN LIMITATIONS](#KNOWN_LIMITATIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                          |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-REFS(1)                     Git Manual                    GIT-REFS(1)

## [](#NAME)NAME

           git-refs - Low-level access to refs

## [](#SYNOPSIS)SYNOPSIS

           git refs migrate --ref-format=<format> [--no-reflog] [--dry-run]
           git refs verify [--strict] [--verbose]
           git refs list [--count=<count>] [--shell|--perl|--python|--tcl]
                              [(--sort=<key>)...] [--format=<format>]
                              [--include-root-refs] [--points-at=<object>]
                              [--merged[=<object>]] [--no-merged[=<object>]]
                              [--contains[=<object>]] [--no-contains[=<object>]]
                              [(--exclude=<pattern>)...] [--start-after=<marker>]
                              [ --stdin | (<pattern>...)]
           git refs exists <ref>
           git refs optimize [--all] [--no-prune] [--auto] [--include <pattern>] [--exclude <pattern>]
           git refs create [--message=<reason>] [--no-deref] [--create-reflog] <ref> <new-value>
           git refs delete [--message=<reason>] [--no-deref] <ref> [<old-value>]
           git refs update [--message=<reason>] [--no-deref] [--create-reflog] <ref> <new-value> [<old-value>]
           git refs rename [--message=<reason>] <old-ref> <new-ref>

## [](#DESCRIPTION)DESCRIPTION

           This command provides low-level access to refs.

## [](#COMMANDS)COMMANDS

           migrate
               Migrate ref store between different formats.

           verify
               Verify reference database consistency.

           list
               List references in the repository with support for filtering,
               formatting, and sorting. This subcommand is an alias for
               git-for-each-ref(1) and offers identical functionality.

           exists
               Check whether the given reference exists. Returns an exit code
               of 0 if it does, 2 if it is missing, and 1 in case looking up
               the reference failed with an error other than the reference
               being missing. This does not verify whether the reference
               resolves to an actual object.

           optimize
               Optimizes references to improve repository performance and
               reduce disk usage. This subcommand is an alias for
               git-pack-refs(1) and offers identical functionality.

           create
               Create the given reference, which must not already exist,
               pointing at <new-value>.

           delete
               Delete the given reference. This subcommand mirrors git
               update-ref -d (see git-update-ref(1)). When <old-value> is
               given, the reference is only deleted after verifying that it
               currently contains <old-value>.

           update
               Update the given reference to point at <new-value>. If
               <old-value> is given, the reference is only updated after
               verifying that it currently contains <old-value>. As a special
               case, an all-zeroes <new-value> deletes the branch, whereas an
               all-zeroes <old-value> ensures that the branch does not yet
               exist.

           rename
               Rename the reference <oldref> to <newref>. The old reference
               must exist and the new reference must not yet exist, and both
               must have a well-formed name (see git-check-ref-format(1)).

## [](#OPTIONS)OPTIONS

           The following options are specific to git refs migrate:

           --ref-format=<format>
               The ref format to migrate the ref store to. Can be one of:

               files
                   for loose files with packed-refs. This is the default.

               reftable
                   for the reftable format.

           --dry-run
               Perform the migration, but do not modify the repository. The
               migrated refs will be written into a separate directory that
               can be inspected separately. The name of the directory will be
               reported on stdout. This can be used to double check that the
               migration works as expected before performing the actual
               migration.

           --reflog, --no-reflog
               Choose between migrating the reflog data to the new backend,
               and discarding them. The default is "--reflog", to migrate.

           The following options are specific to git refs verify:

           --strict
               Enable stricter error checking. This will cause warnings to be
               reported as errors. See git-fsck(1).

           --verbose
               When verifying the reference database consistency, be chatty.

           The following options are specific to git refs list:

           <pattern>...
               If one or more <pattern> parameters are given, only refs are
               shown that match against at least one pattern, either using
               fnmatch(3) or literally, in the latter case matching
               completely or from the beginning up to a slash.

           --stdin
               The list of patterns is read from standard input instead of
               from the argument list.

           --count=<count>
               Stop after showing <count> refs.

           --sort=<key>
               Sort on the field name <key>. Prefix - to sort in descending
               order of the value. When unspecified, refname is used. You may
               use the --sort=<key> option multiple times, in which case the
               last key becomes the primary key.

           --format[=<format>]
               A string that interpolates %(fieldname) from a ref being shown
               and the object it points at. In addition, the string literal
               %% renders as % and %xx - where xx are hex digits - renders as
               the character with hex code xx. For example, %00 interpolates
               to \0 (NUL), %09 to \t (TAB), and %0a to \n (LF).

           When unspecified, <format> defaults to %(objectname) SPC
           %(objecttype) TAB %(refname).

           --color[=<when>]
               Respect any colors specified in the --format option. The
               <when> field must be one of always, never, or auto (if <when>
               is absent, behave as if always was given).

           --shell, --perl, --python, --tcl
               If given, strings that substitute %(fieldname) placeholders
               are quoted as string literals suitable for the specified host
               language. This is meant to produce a scriptlet that can
               directly be "eval"ed.

           --points-at=<object>
               Only list refs which points at the given object.

           --merged[=<object>]
               Only list refs whose tips are reachable from the specified
               commit (HEAD if not specified).

           --no-merged[=<object>]
               Only list refs whose tips are not reachable from <object>(HEAD
               if not specified).

           --contains[=<object>]
               Only list refs which contain <object>(HEAD if not specified).

           --no-contains[=<object>]
               Only list refs which don’t contain <object> (HEAD if not
               specified).

           --ignore-case
               Sorting and filtering refs are case insensitive.

           --omit-empty
               Do not print a newline after formatted refs where the format
               expands to the empty string.

           --exclude=<excluded-pattern>
               If one or more --exclude options are given, only refs which do
               not match any <excluded-pattern> parameters are shown.
               Matching is done using the same rules as <pattern> above.

           --include-root-refs
               List root refs (HEAD and pseudorefs) apart from regular refs.

           --start-after=<marker>
               Allows paginating the output by skipping references up to and
               including the specified marker. When paging, it should be
               noted that references may be deleted, modified or added
               between invocations. Output will only yield those references
               which follow the marker lexicographically. Output begins from
               the first reference that would come after the marker
               alphabetically. Cannot be used with --sort=<key> or --stdin
               options, or the <pattern> argument(s) to limit the refs.

           The following options are specific to git refs optimize:

           --all
               The command by default packs all tags and refs that are
               already packed, and leaves other refs alone. This is because
               branches are expected to be actively developed and packing
               their tips does not help performance. This option causes all
               refs to be packed as well, with the exception of hidden refs,
               broken refs, and symbolic refs. Useful for a repository with
               many branches of historical interests.

           --no-prune
               The command usually removes loose refs under $GIT_DIR/refs
               hierarchy after packing them. This option tells it not to.

           --auto
               Pack refs as needed depending on the current state of the ref
               database. The behavior depends on the ref format used by the
               repository and may change in the future.

               •   "files": Loose references are packed into the packed-refs
                   file based on the ratio of loose references to the size of
                   the packed-refs file. The bigger the packed-refs file, the
                   more loose references need to exist before we repack.

               •   "reftable": Tables are compacted such that they form a
                   geometric sequence. For two tables N and N+1, where N+1 is
                   newer, this maintains the property that N is at least
                   twice as big as N+1. Only tables that violate this
                   property are compacted.

           --include <pattern>
               Pack refs based on a glob(7) pattern. Repetitions of this
               option accumulate inclusion patterns. If a ref is both
               included in --include and --exclude, --exclude takes
               precedence. Using --include will preclude all tags from being
               included by default. Symbolic refs and broken refs will never
               be packed. When used with --all, it will be a noop. Use
               --no-include to clear and reset the list of patterns.

           --exclude <pattern>
               Do not pack refs matching the given glob(7) pattern.
               Repetitions of this option accumulate exclusion patterns. Use
               --no-exclude to clear and reset the list of patterns. If a ref
               is already packed, including it with --exclude will not unpack
               it.

               When used with --all, pack only loose refs which do not match
               any of the provided --exclude patterns.

               When used with --include, refs provided to --include, minus
               refs that are provided to --exclude will be packed.

           The following options are specific to commands which write
           references:

           --create-reflog
               Create a reflog for the reference even if one would not
               ordinarily be created.

           --message=<reason>
               Use the given <reason> string for the reflog entry associated
               with the update. An empty message is rejected.

           --no-deref
               Operate on <ref> itself rather than the reference it points to
               via a symbolic ref.

## [](#KNOWN_LIMITATIONS)KNOWN LIMITATIONS

           The ref format migration has several known limitations in its
           current form:

           •   It is not possible to migrate repositories that have
               worktrees.

           •   There is no way to block concurrent writes to the repository
               during an ongoing migration. Concurrent writes can lead to an
               inconsistent migrated state. Users are expected to block
               writes on a higher level. If your repository is registered for
               scheduled maintenance, it is recommended to unregister it
               first with git-maintenance(1).

           These limitations may eventually be lifted.

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

    Git 2.55.0.493.g5b2471          2026-08-03                    GIT-REFS(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-fsck(1)](../man1/git-fsck.1.html)

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
