---
{"title": "git-fetch-pack(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-fetch-pack.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-fetch-pack(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-FETCH-PACK(1)               Git Manual              GIT-FETCH-PACK(1)

## [](#NAME)NAME

           git-fetch-pack - Receive missing objects from another repository

## [](#SYNOPSIS)SYNOPSIS

           git fetch-pack [--all] [--quiet|-q] [--keep|-k] [--thin] [--include-tag]
                   [--upload-pack=<git-upload-pack>]
                   [--depth=<n>] [--no-progress]
                   [-v] <repository> [<refs>...]

## [](#DESCRIPTION)DESCRIPTION

           Usually you would want to use git fetch, which is a higher level
           wrapper of this command, instead.

           Invokes git-upload-pack on a possibly remote repository and asks
           it to send objects missing from this repository, to update the
           named heads. The list of commits available locally is found out by
           scanning the local refs/ hierarchy and sent to git-upload-pack
           running on the other end.

           This command degenerates to download everything to complete the
           asked refs from the remote side when the local side does not have
           a common ancestor commit.

## [](#OPTIONS)OPTIONS

           --all
               Fetch all remote refs.

           --stdin
               Take the list of refs from stdin, one per line. If there are
               refs specified on the command line in addition to this option,
               then the refs from stdin are processed after those on the
               command line.

               If --stateless-rpc is specified together with this option then
               the list of refs must be in packet format (pkt-line). Each ref
               must be in a separate packet, and the list must end with a
               flush packet.

           -q, --quiet
               Pass -q flag to git unpack-objects; this makes the cloning
               process less verbose.

           -k, --keep
               Do not invoke git unpack-objects on received data, but create
               a single packfile out of it instead, and store it in the
               object database. If provided twice then the pack is locked
               against repacking.

           --thin
               Fetch a "thin" pack, which records objects in deltified form
               based on objects not included in the pack to reduce network
               traffic.

           --include-tag
               If the remote side supports it, annotated tags objects will be
               downloaded on the same connection as the other objects if the
               object the tag references is downloaded. The caller must
               otherwise determine the tags this option made available.

           --upload-pack=<git-upload-pack>
               Use this to specify the path to git-upload-pack on the remote
               side, if it is not found on your $PATH. Installations of sshd
               ignores the user’s environment setup scripts for login shells
               (e.g. .bash_profile) and your privately installed git may not
               be found on the system default $PATH. Another workaround
               suggested is to set up your $PATH in ".bashrc", but this flag
               is for people who do not want to pay the overhead for
               non-interactive shells by having a lean .bashrc file (they set
               most of the things up in .bash_profile).

           --exec=<git-upload-pack>
               Same as --upload-pack=<git-upload-pack>.

           --depth=<n>
               Limit fetching to ancestor-chains not longer than n.
               git-upload-pack treats the special depth 2147483647 as
               infinite even if there is an ancestor-chain that long.

           --shallow-since=<date>
               Deepen or shorten the history of a shallow repository to
               include all reachable commits after <date>.

           --shallow-exclude=<ref>
               Deepen or shorten the history of a shallow repository to
               exclude commits reachable from a specified remote branch or
               tag. This option can be specified multiple times.

           --deepen-relative
               Argument --depth specifies the number of commits from the
               current shallow boundary instead of from the tip of each
               remote branch history.

           --refetch
               Skips negotiating commits with the server in order to fetch
               all matching objects. Use to reapply a new partial clone
               blob/tree filter.

           --no-progress
               Do not show the progress.

           --check-self-contained-and-connected
               Output "connectivity-ok" if the received pack is
               self-contained and connected.

           -v
               Run verbosely.

           <repository>
               The URL to the remote repository.

           <refs>...
               The remote heads to update from. This is relative to $GIT_DIR
               (e.g. "HEAD", "refs/heads/master"). When unspecified, update
               from all heads the remote side has.

               If the remote has enabled the options
               uploadpack.allowTipSHA1InWant,
               uploadpack.allowReachableSHA1InWant, or
               uploadpack.allowAnySHA1InWant, they may alternatively be
               40-hex sha1s present on the remote.

## [](#SEE_ALSO)SEE ALSO

           git-fetch(1)

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

    Git 2.55.0.493.g5b2471          2026-08-03              GIT-FETCH-PACK(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-config(1)](../man1/git-config.1.html),  [git-fetch(1)](../man1/git-fetch.1.html),  [git-receive-pack(1)](../man1/git-receive-pack.1.html)

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
