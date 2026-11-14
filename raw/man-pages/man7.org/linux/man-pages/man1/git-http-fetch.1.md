---
{"title": "git-http-fetch(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-http-fetch.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-http-fetch(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-HTTP-FETCH(1)               Git Manual              GIT-HTTP-FETCH(1)

## [](#NAME)NAME

           git-http-fetch - Download from a remote Git repository via HTTP

## [](#SYNOPSIS)SYNOPSIS

           git http-fetch [-c] [-t] [-a] [-d] [-v] [-w <filename>] [--recover] [--stdin | --packfile=<hash> | <commit>] <URL>

## [](#DESCRIPTION)DESCRIPTION

           Downloads a remote Git repository via HTTP.

           This command always gets all objects. Historically, there were
           three options -a, -c and -t for choosing which objects to
           download. They are now silently ignored.

## [](#OPTIONS)OPTIONS

           commit-id
               Either the hash or the filename under [URL]/refs/ to pull.

           -a, -c, -t
               These options are ignored for historical reasons.

           -v
               Report what is downloaded.

           -w <filename>
               Writes the commit-id into the specified filename under
               $GIT_DIR/refs/<filename> on the local end after the transfer
               is complete.

           --stdin
               Instead of a commit id on the command line (which is not
               expected in this case), git http-fetch expects lines on stdin
               in the format

                   <commit-id>['\t'<filename-as-in--w>]

           --packfile=<hash>
               For internal use only. Instead of a commit id on the command
               line (which is not expected in this case), git http-fetch
               fetches the packfile directly at the given URL and uses
               index-pack to generate corresponding .idx and .keep files. The
               hash is used to determine the name of the temporary file and
               is arbitrary. The output of index-pack is printed to stdout.
               Requires --index-pack-args.

           --index-pack-args=<args>
               For internal use only. The command to run on the contents of
               the downloaded pack. Arguments are URL-encoded separated by
               spaces.

           --recover
               Verify that everything reachable from target is fetched. Used
               after an earlier fetch is interrupted.

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

    Git 2.55.0.493.g5b2471          2026-08-03              GIT-HTTP-FETCH(1)

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
