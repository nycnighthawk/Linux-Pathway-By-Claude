---
{"title": "git-format-rev(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-format-rev.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-format-rev(1) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [INPUT AND OUTPUT FORMAT](#INPUT_AND_OUTPUT_FORMAT) \| [EXAMPLES](#EXAMPLES) \| [DISCUSSION](#DISCUSSION) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                            |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-FORMAT-REV(1)               Git Manual              GIT-FORMAT-REV(1)

## [](#NAME)NAME

           git-format-rev - EXPERIMENTAL: Pretty format revisions on demand

## [](#SYNOPSIS)SYNOPSIS

           (EXPERIMENTAL!) git format-rev --stdin-mode=<mode> --format=<pretty> [--[no-]notes=<ref>] [-z] [--[no-]null-output] [--[no-]null-input]

## [](#DESCRIPTION)DESCRIPTION

           Pretty format revisions from standard input.

           THIS COMMAND IS EXPERIMENTAL. THE BEHAVIOR MAY CHANGE.

## [](#OPTIONS)OPTIONS

           --stdin-mode=<mode>
               How to interpret standard input data:

               revs
                   Each line or record (see the INPUT AND OUTPUT FORMATS
                   section) is interpreted as a commit. Any kind of revision
                   expression can be used (see gitrevisions(7)). Annotated
                   tags are peeled (see gitglossary(7)).

                   The argument rev is also accepted.

               text
                   Formats all commit object names found in freeform text.
                   These must be full object names, i.e. abbreviated
                   hexadecimal object names will not be interpreted.

                   Anything that is parsed as an object name but that is not
                   found to be a commit object name is left alone (echoed).

           --format=<pretty>
               Pretty format string.

           --notes=<ref>, --no-notes
               Custom notes ref. Notes are displayed when using the %N atom.
               See git-notes(1).

           -z, --null
               Use NUL character to terminate both input and output instead
               of newline. This option cannot be negated.

               This is useful if both the input and output could contain
               newlines or if the input to this command also uses NUL
               character termination; see the INPUT AND OUTPUT FORMATS
               section below.

               The mode --stdin-mode=text can have use for this option when
               it needs to process input like for example git last-modified
               -z; see the EXAMPLES section below.

           --null-output, --no-null-output
               Use NUL character to terminate output instead of newline. The
               default is --no-null-output.

               This is useful if the output could contain newlines, for
               example if the %n (newline) atom is used.

           --null-input, --no-null-input
               Use NUL character to terminate input instead of newline. The
               default is --no-null-input.

               This is useful if the input revision expressions could contain
               newlines.

## [](#INPUT_AND_OUTPUT_FORMAT)INPUT AND OUTPUT FORMAT

           The command uses newlines for both input and output termination by
           default. See the -z, --null-output, and --null-input options for
           using NUL character as the terminator.

           The mode --stdin-mode=revs outputs one formatted commit followed
           by the terminator. This could either be called a line or a record
           in case "line" is too suggestive of newline termination.

           Note that this means that the terminator character (newline or
           NUL) acts as a terminator, not a separator. In other words, the
           final line or record is also terminated by the terminator
           character.

           The mode --stdin-mode=text replaces each object name with the
           formatted commit, i.e. the format %s would transform some commit
           object name to <subject> without any termination. Like this:

               Did we not fix this in "<subject>"?

           It is safe to interactively read and write from this command since
           each record is immediately flushed.

## [](#EXAMPLES)EXAMPLES

           The command git-last-modified(1) shows the commit that each file
           was last modified in.

               $ git last-modified -- README.md Makefile
               7798034171030be0909c56377a4e0e10e6d2df93        Makefile
               c50fbb2dd225e7e82abba4380423ae105089f4d7        README.md

           We can pipe the result to this command in order to replace the
           object name with the commit author.

               $ git last-modified -- README.md Makefile |
                   git format-rev --stdin-mode=text --format=%an
               Junio C Hamano  Makefile
               Todd Zullinger  README.md

           Another example is formatting commits in commit messages. Given
           this commit message:

               Fix off-by-one error

               Fix off-by-one error introduced in
               e83c5163316f89bfbde7d9ab23ca2e25604af290.

               We thought we fixed this in 5569bf9bbedd63a00780fc5c110e0cfab3aa97b9 but
               that only covered 1/3 of the faulty cases.

           We can format the commits and use par(1) to reflow the text, say
           in a commit-msg hook:

               $ git config set hook.reference-commits.event commit-msg
               $ git config set hook.reference-commits.command reference-commits
               $ cat $(which reference-commits)
               #/bin/sh

               msg="$1"
               rewritten=$(mktemp)
               git format-rev --stdin-mode=text --format=reference <"$msg" |
                   par >"$rewritten"
               mv "$rewritten" "$msg"

           Which will produce something like this:

               Fix off-by-one error

               Fix off-by-one error introduced in e83c5163316 (Implement better memory
               allocator, 2005-04-07).

               We thought we fixed this in 5569bf9bbed (Fix memory allocator,
               2005-06-22) but that only covered 1/3 of the faulty cases.

## [](#DISCUSSION)DISCUSSION

           This command lets you format any number of revisions in any order
           through one command invocation. Consider the git-last-modified(1)
           case from the EXAMPLES section above:

            1. There might be hundreds of files

            2. Commits can be repeated, i.e. two or more files were last
               modified in the same commit

           Two widely-used commands which pretty formats commits are
           git-log(1) and git-show(1). It turns out that they are not a good
           fit for the above use case.

           •   The output of git-last-modified(1) would have to be processed
               in stages since you need to transform the first column
               separately and then link the author to the filename. But this
               is surmountable.

           •   You can feed each commit to git show or git log --no-walk -1.
               But that means that you need to create a process for each
               line.

           •   Let’s say that you want to use one process, not one per line.
               So you want to feed all the commits to the command. Now you
               face the problem that you have to feed all the commits to the
               commands before you get any output (this is also the case for
               the --stdin modes). In other words, you cannot loop through
               each line, get the author for the commit, and output the
               author and the filename. You need to feed all the commits, get
               back all the output, and match the output with the filename.

           •   But the next problem is that commands will deduplicate the
               input and only output one commit one single time only. Thus
               you cannot make the output order match the input order, since
               a commit could have been repeated in the original input.

           In short, it is straightforward to use these two commands if you
           use one process per line. It is much more work if you just want to
           use one process, but still doable. In contrast, this problem is
           solved with just another shell pipeline with this command.

## [](#SEE_ALSO)SEE ALSO

           git-name-rev(1), git-log(1).

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

    Git 2.55.0.493.g5b2471          2026-08-03              GIT-FORMAT-REV(1)

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
