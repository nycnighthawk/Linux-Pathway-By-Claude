---
{"title": "git-name-rev(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-name-rev.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-name-rev(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-NAME-REV(1)                 Git Manual                GIT-NAME-REV(1)

## [](#NAME)NAME

           git-name-rev - Find symbolic names for given revs

## [](#SYNOPSIS)SYNOPSIS

           git name-rev [--tags] [--refs=<pattern>]
                          ( --all | --annotate-stdin | <commit-ish>... )

## [](#DESCRIPTION)DESCRIPTION

           Finds symbolic names suitable for human digestion for revisions
           given in any format parsable by git rev-parse.

## [](#OPTIONS)OPTIONS

           --tags
               Do not use branch names, but only tags to name the commits

           --refs=<pattern>
               Only use refs whose names match a given shell pattern. The
               pattern can be a branch name, a tag name, or a fully qualified
               ref name. If given multiple times, use refs whose names match
               any of the given shell patterns. Use --no-refs to clear any
               previous ref patterns given.

           --exclude=<pattern>
               Do not use any ref whose name matches a given shell pattern.
               The pattern can be one of branch name, tag name or fully
               qualified ref name. If given multiple times, a ref will be
               excluded when it matches any of the given patterns. When used
               together with --refs, a ref will be used as a match only when
               it matches at least one --refs pattern and does not match any
               --exclude patterns. Use --no-exclude to clear the list of
               exclude patterns.

           --all
               List all commits reachable from all refs

           --annotate-stdin
               Transform stdin by substituting all the 40-character SHA-1
               hexes (say $hex) with "$hex ($rev_name)". When used with
               --name-only, substitute with "$rev_name", omitting $hex
               altogether. This option was called --stdin in older versions
               of Git.

               For example:

                   $ cat sample.txt

                   An abbreviated revision 2ae0a9cb82 will not be substituted.
                   The full name after substitution is 2ae0a9cb8298185a94e5998086f380a355dd8907,
                   while its tree object is 70d105cc79e63b81cfdcb08a15297c23e60b07ad

                   $ git name-rev --annotate-stdin <sample.txt

                   An abbreviated revision 2ae0a9cb82 will not be substituted.
                   The full name after substitution is 2ae0a9cb8298185a94e5998086f380a355dd8907 (master),
                   while its tree object is 70d105cc79e63b81cfdcb08a15297c23e60b07ad

                   $ git name-rev --name-only --annotate-stdin <sample.txt

                   An abbreviated revision 2ae0a9cb82 will not be substituted.
                   The full name after substitution is master,
                   while its tree object is 70d105cc79e63b81cfdcb08a15297c23e60b07ad

           --name-only
               Instead of printing both the SHA-1 and the name, print only
               the name. If given with --tags the usual tag prefix of "tags/"
               is also omitted from the name, matching the output of
               git-describe more closely.

           --no-undefined
               Die with error code != 0 when a reference is undefined,
               instead of printing undefined.

           --always
               Show uniquely abbreviated commit object as fallback.

## [](#EXAMPLES)EXAMPLES

           Given a commit, find out where it is relative to the local refs.
           Say somebody wrote you about that fantastic commit
           33db5f4d9027a10e477ccf054b2c1ab94f74c85a. Of course, you look into
           the commit, but that only tells you what happened, but not the
           context.

           Enter git name-rev:

               % git name-rev 33db5f4d9027a10e477ccf054b2c1ab94f74c85a
               33db5f4d9027a10e477ccf054b2c1ab94f74c85a tags/v0.99~940

           Now you are wiser, because you know that it happened 940 revisions
           before v0.99.

           Another nice thing you can do is:

               % git log | git name-rev --annotate-stdin

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

    Git 2.55.0.493.g5b2471          2026-08-03                GIT-NAME-REV(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-format-rev(1)](../man1/git-format-rev.1.html)

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
