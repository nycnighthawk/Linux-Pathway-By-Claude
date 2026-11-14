---
{"title": "git-commit-tree(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-commit-tree.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-commit-tree(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMMIT INFORMATION](#COMMIT_INFORMATION) \| [DATE FORMATS](#DATE_FORMATS) \| [DISCUSSION](#DISCUSSION) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                             |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-COMMIT-TREE(1)              Git Manual             GIT-COMMIT-TREE(1)

## [](#NAME)NAME

           git-commit-tree - Create a new commit object

## [](#SYNOPSIS)SYNOPSIS

           git commit-tree <tree> [(-p <parent>)...]
           git commit-tree [(-p <parent>)...] [-S[<keyid>]] [(-m <message>)...]
                             [(-F <file>)...] <tree>

## [](#DESCRIPTION)DESCRIPTION

           This is usually not what an end user wants to run directly. See
           git-commit(1) instead.

           Creates a new commit object based on the provided tree object and
           emits the new commit object id on stdout. The log message is read
           from the standard input, unless -m or -F options are given.

           The -m and -F options can be given any number of times, in any
           order. The commit log message will be composed in the order in
           which the options are given.

           A commit object may have any number of parents. With exactly one
           parent, it is an ordinary commit. Having more than one parent
           makes the commit a merge between several lines of history. Initial
           (root) commits have no parents.

           While a tree represents a particular directory state of a working
           directory, a commit represents that state in "time", and explains
           how to get there.

           Normally a commit would identify a new "HEAD" state, and while Git
           doesn’t care where you save the note about that state, in practice
           we tend to just write the result to the file that is pointed at by
           .git/HEAD, so that we can always see what the last committed state
           was.

## [](#OPTIONS)OPTIONS

           <tree>
               An existing tree object.

           -p <parent>
               Each -p indicates the id of a parent commit object.

           -m <message>
               A paragraph in the commit log message. This can be given more
               than once and each <message> becomes its own paragraph.

           -F <file>
               Read the commit log message from the given file. Use - to read
               from the standard input. This can be given more than once and
               the content of each file becomes its own paragraph.

           -S[<keyid>], --gpg-sign[=<keyid>], --no-gpg-sign
               GPG-sign commits. The keyid argument is optional and defaults
               to the committer identity; if specified, it must be stuck to
               the option without a space.  --no-gpg-sign is useful to
               countermand a --gpg-sign option given earlier on the command
               line.

## [](#COMMIT_INFORMATION)COMMIT INFORMATION

           A commit encapsulates:

           •   all parent object ids

           •   author name, email and date

           •   committer name and email and the commit time.

           A commit comment is read from stdin. If a changelog entry is not
           provided via "<" redirection, git commit-tree will just wait for
           one to be entered and terminated with ^D.

## [](#DATE_FORMATS)DATE FORMATS

           The GIT_AUTHOR_DATE and GIT_COMMITTER_DATE environment variables
           support the following date formats:

           Git internal format
               It is <unix-timestamp> <time-zone-offset>, where
               <unix-timestamp> is the number of seconds since the UNIX
               epoch.  <time-zone-offset> is a positive or negative offset
               from UTC. For example CET (which is 1 hour ahead of UTC) is
               +0100.

               It is safer to prepend the <unix-timestamp> with @ (e.g., @0
               +0000), which forces Git to interpret it as a raw timestamp.
               This is required for values less than 100,000,000 (which have
               fewer than 9 digits) to avoid confusion with other date
               formats like YYYYMMDD.

           RFC 2822
               The standard date format as described by RFC 2822, for example
               Thu, 07 Apr 2005 22:13:13 +0200.

           ISO 8601
               Time and date specified by the ISO 8601 standard, for example
               2005-04-07T22:13:13. The parser accepts a space instead of the
               T character as well. Fractional parts of a second will be
               ignored, for example 2005-04-07T22:13:13.019 will be treated
               as 2005-04-07T22:13:13.

                   Note
                   In addition, the date part is accepted in the following
                   formats: YYYY.MM.DD, MM/DD/YYYY and DD.MM.YYYY.

## [](#DISCUSSION)DISCUSSION

           Git is to some extent character encoding agnostic.

           •   The contents of the blob objects are uninterpreted sequences
               of bytes. There is no encoding translation at the core level.

           •   Path names are encoded in UTF-8 normalization form C. This
               applies to tree objects, the index file, ref names, as well as
               path names in command line arguments, environment variables
               and config files (.git/config (see git-config(1)),
               gitignore(5), gitattributes(5) and gitmodules(5)).

               Note that Git at the core level treats path names simply as
               sequences of non-NUL bytes, there are no path name encoding
               conversions (except on Mac and Windows). Therefore, using
               non-ASCII path names will mostly work even on platforms and
               file systems that use legacy extended ASCII encodings.
               However, repositories created on such systems will not work
               properly on UTF-8-based systems (e.g. Linux, Mac, Windows) and
               vice versa. Additionally, many Git-based tools simply assume
               path names to be UTF-8 and will fail to display other
               encodings correctly.

           •   Commit log messages are typically encoded in UTF-8, but other
               extended ASCII encodings are also supported. This includes
               ISO-8859-x, CP125x and many others, but not UTF-16/32, EBCDIC
               and CJK multi-byte encodings (GBK, Shift-JIS, Big5, EUC-x,
               CP9xx etc.).

           Although we encourage that the commit log messages are encoded in
           UTF-8, both the core and Git Porcelain are designed not to force
           UTF-8 on projects. If all participants of a particular project
           find it more convenient to use legacy encodings, Git does not
           forbid it. However, there are a few things to keep in mind.

            1. git commit and git commit-tree issue a warning if the commit
               log message given to it does not look like a valid UTF-8
               string, unless you explicitly say your project uses a legacy
               encoding. The way to say this is to have i18n.commitEncoding
               in .git/config file, like this:

                   [i18n]
                           commitEncoding = ISO-8859-1

               Commit objects created with the above setting record the value
               of i18n.commitEncoding in their encoding header. This is to
               help other people who look at them later. Lack of this header
               implies that the commit log message is encoded in UTF-8.

            2. git log, git show, git blame and friends look at the encoding
               header of a commit object, and try to re-code the log message
               into UTF-8 unless otherwise specified. You can specify the
               desired output encoding with i18n.logOutputEncoding in
               .git/config file, like this:

                   [i18n]
                           logOutputEncoding = ISO-8859-1

               If you do not have this configuration variable, the value of
               i18n.commitEncoding is used instead.

           Note that we deliberately chose not to re-code the commit log
           message when a commit is made to force UTF-8 at the commit object
           level, because re-coding to UTF-8 is not necessarily a reversible
           operation.

## [](#FILES)FILES

           /etc/mailname

## [](#SEE_ALSO)SEE ALSO

           git-write-tree(1) git-commit(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-COMMIT-TREE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-commit(1)](../man1/git-commit.1.html),  [git-filter-branch(1)](../man1/git-filter-branch.1.html),  [git-merge-tree(1)](../man1/git-merge-tree.1.html),  [git-var(1)](../man1/git-var.1.html)

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
