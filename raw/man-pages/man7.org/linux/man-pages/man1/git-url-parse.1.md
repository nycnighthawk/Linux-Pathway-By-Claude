---
{"title": "git-url-parse(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-url-parse.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-url-parse(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [OUTPUT](#OUTPUT) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                             |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-URL-PARSE(1)                Git Manual               GIT-URL-PARSE(1)

## [](#NAME)NAME

           git-url-parse - Parse and extract git URL components

## [](#SYNOPSIS)SYNOPSIS

           git url-parse [-c <component>] [--] <url>...

## [](#DESCRIPTION)DESCRIPTION

           Git supports many ways to specify URLs, some of them non-standard.
           For example, git supports the scp style [user@]host:[path] format.
           This command eases interoperability with git URLs by enabling the
           parsing and extraction of the components of all git URLs.

           Any syntactically valid URL is parsed, even if the scheme is not
           one git supports for fetching or pushing.

## [](#OPTIONS)OPTIONS

           -c <component>, --component <component>
               Extract the <component> component from the given Git URLs.
               <component> can be one of: scheme, user, password, host, port,
               path.

## [](#OUTPUT)OUTPUT

           When --component is given, the requested component of each URL is
           printed on its own line, in the order the URLs were given. If the
           URL has no such component (for example, a port in a URL that does
           not specify one), an empty line is printed in its place.

           When --component is not given, no output is produced. The exit
           status is zero if every URL parses successfully and non-zero
           otherwise, allowing the command to be used purely as a validator.

## [](#EXAMPLES)EXAMPLES

           •   Print the host name:

                   $ git url-parse --component host https://example.com/user/repo
                   example.com

           •   Print the path:

                   $ git url-parse --component path https://example.com/user/repo
                   /user/repo
                   $ git url-parse --component path example.com:~user/repo
                   ~user/repo
                   $ git url-parse --component path example.com:user/repo
                   /user/repo

           •   Validate URLs without outputting anything:

                   $ git url-parse https://example.com/user/repo example.com:~user/repo

## [](#SEE_ALSO)SEE ALSO

           git-clone(1), git-fetch(1), git-config(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03               GIT-URL-PARSE(1)

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
