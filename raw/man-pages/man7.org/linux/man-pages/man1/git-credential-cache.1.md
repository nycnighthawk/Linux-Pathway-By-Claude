---
{"title": "git-credential-cache(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-credential-cache.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-credential-cache(1) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [CONTROLLING THE DAEMON](#CONTROLLING_THE_DAEMON) \| [EXAMPLES](#EXAMPLES) \| [PERSONAL ACCESS TOKENS](#PERSONAL_ACCESS_TOKENS) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-CREDENTIAL-CACHE(1)         Git Manual        GIT-CREDENTIAL-CACHE(1)

## [](#NAME)NAME

           git-credential-cache - Helper to temporarily store passwords in
           memory

## [](#SYNOPSIS)SYNOPSIS

           git config credential.helper 'cache [<options>]'

## [](#DESCRIPTION)DESCRIPTION

           This command caches credentials for use by future Git programs.
           The stored credentials are kept in memory of the cache-daemon
           process (instead of being written to a file) and are forgotten
           after a configurable timeout. Credentials are forgotten sooner if
           the cache-daemon dies, for example if the system restarts. The
           cache is accessible over a Unix domain socket, restricted to the
           current user by filesystem permissions.

           You probably don’t want to invoke this command directly; it is
           meant to be used as a credential helper by other parts of Git. See
           gitcredentials(7) or EXAMPLES below.

## [](#OPTIONS)OPTIONS

           --timeout <seconds>
               Number of seconds to cache credentials (default: 900).

           --socket <path>
               Use <path> to contact a running cache daemon (or start a new
               cache daemon if one is not started). Defaults to
               $XDG_CACHE_HOME/git/credential/socket unless
               ~/.git-credential-cache/ exists in which case
               ~/.git-credential-cache/socket is used instead. If your home
               directory is on a network-mounted filesystem, you may need to
               change this to a local filesystem. You must specify an
               absolute path.

## [](#CONTROLLING_THE_DAEMON)CONTROLLING THE DAEMON

           If you would like the daemon to exit early, forgetting all cached
           credentials before their timeout, you can issue an exit action:

               git credential-cache exit

## [](#EXAMPLES)EXAMPLES

           The point of this helper is to reduce the number of times you must
           type your username or password. For example:

               $ git config credential.helper cache
               $ git push http://example.com/repo.git
               Username: <type your username>
               Password: <type your password>

               [work for 5 more minutes]
               $ git push http://example.com/repo.git
               [your credentials are used automatically]

           You can provide options via the credential.helper configuration
           variable (this example increases the cache time to 1 hour):

               $ git config credential.helper 'cache --timeout=3600'

## [](#PERSONAL_ACCESS_TOKENS)PERSONAL ACCESS TOKENS

           Some remotes accept personal access tokens, which are randomly
           generated and hard to memorise. They typically have a lifetime of
           weeks or months.

           git-credential-cache is inherently unsuitable for persistent
           storage of personal access tokens. The credential will be
           forgotten after the cache timeout. Even if you configure a long
           timeout, credentials will be forgotten if the daemon dies.

           To avoid frequently regenerating personal access tokens, configure
           a credential helper with persistent storage. Alternatively,
           configure an OAuth credential helper to generate credentials
           automatically. See gitcredentials(7), sections "Available helpers"
           and "OAuth".

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

    Git 2.55.0.493.g5b2471          2026-08-03        GIT-CREDENTIAL-CACHE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-credential-cache\--daemon(1)](../man1/git-credential-cache--daemon.1.html),  [git-credential-store(1)](../man1/git-credential-store.1.html),  [gitcredentials(7)](../man7/gitcredentials.7.html)

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
