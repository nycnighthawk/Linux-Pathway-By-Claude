---
{"title": "git-upload-pack(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-upload-pack.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-upload-pack(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SECURITY](#SECURITY) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-UPLOAD-PACK(1)              Git Manual             GIT-UPLOAD-PACK(1)

## [](#NAME)NAME

           git-upload-pack - Send objects packed back to git-fetch-pack

## [](#SYNOPSIS)SYNOPSIS

           git-upload-pack [--[no-]strict] [--timeout=<n>] [--stateless-rpc]
                             [--advertise-refs] <directory>

## [](#DESCRIPTION)DESCRIPTION

           Invoked by git fetch-pack, learns what objects the other side is
           missing, and sends them after packing.

           This command is usually not invoked directly by the end user. The
           UI for the protocol is on the git fetch-pack side, and the program
           pair is meant to be used to pull updates from a remote repository.
           For push operations, see git send-pack.

## [](#OPTIONS)OPTIONS

           --strict, --no-strict
               Do not try <directory>/.git/ if <directory> is not a Git
               directory.

           --timeout=<n>
               Interrupt transfer after <n> seconds of inactivity.

           --stateless-rpc
               Perform only a single read-write cycle with stdin and stdout.
               This fits with the HTTP POST request processing model where a
               program may read the request, write a response, and must exit.

           --http-backend-info-refs
               Used by git-http-backend(1) to serve up
               $GIT_URL/info/refs?service=git-upload-pack requests. See
               "Smart Clients" in gitprotocol-http(5) and "HTTP Transport" in
               the gitprotocol-v2(5) documentation. Also understood by
               git-receive-pack(1).

           <directory>
               The repository to sync from.

## [](#ENVIRONMENT)ENVIRONMENT

           GIT_PROTOCOL
               Internal variable used for handshaking the wire protocol.
               Server admins may need to configure some transports to allow
               this variable to be passed. See the discussion in git(1).

           GIT_NO_LAZY_FETCH
               When cloning or fetching from a partial repository (i.e., one
               itself cloned with --filter), the server-side upload-pack may
               need to fetch extra objects from its upstream in order to
               complete the request. By default, upload-pack will refuse to
               perform such a lazy fetch, because git fetch may run arbitrary
               commands specified in configuration and hooks of the source
               repository (and upload-pack tries to be safe to run even in
               untrusted .git directories).

               This is implemented by having upload-pack internally set the
               GIT_NO_LAZY_FETCH variable to 1. If you want to override it
               (because you are fetching from a partial clone, and you are
               sure you trust it), you can explicitly set GIT_NO_LAZY_FETCH
               to 0.

## [](#SECURITY)SECURITY

           Most Git commands should not be run in an untrusted .git directory
           (see the section SECURITY in git(1)). upload-pack tries to avoid
           any dangerous configuration options or hooks from the repository
           it’s serving, making it safe to clone an untrusted directory and
           run commands on the resulting clone.

           For an extra level of safety, you may be able to run upload-pack
           as an alternate user. The details will be platform dependent, but
           on many systems you can run:

               git clone --no-local --upload-pack='sudo -u nobody git-upload-pack' ...

## [](#SEE_ALSO)SEE ALSO

           gitnamespaces(7)

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

    Git 2.55.0.493.g5b2471          2026-08-03             GIT-UPLOAD-PACK(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-receive-pack(1)](../man1/git-receive-pack.1.html),  [gitprotocol-http(5)](../man5/gitprotocol-http.5.html),  [gitprotocol-v2(5)](../man5/gitprotocol-v2.5.html),  [gitnamespaces(7)](../man7/gitnamespaces.7.html)

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
