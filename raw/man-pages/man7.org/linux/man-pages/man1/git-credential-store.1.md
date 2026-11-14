---
{"title": "git-credential-store(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-credential-store.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-credential-store(1) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [EXAMPLES](#EXAMPLES) \| [STORAGE FORMAT](#STORAGE_FORMAT) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-CREDENTIAL-STORE(1)         Git Manual        GIT-CREDENTIAL-STORE(1)

## [](#NAME)NAME

           git-credential-store - Helper to store credentials on disk

## [](#SYNOPSIS)SYNOPSIS

           git config credential.helper 'store [<options>]'

## [](#DESCRIPTION)DESCRIPTION

               Note

               Using this helper will store your passwords unencrypted on
               disk, protected only by filesystem permissions. If this is not
               an acceptable security tradeoff, try git-credential-cache(1),
               or find a helper that integrates with secure storage provided
               by your operating system.

           This command stores credentials indefinitely on disk for use by
           future Git programs.

           You probably don’t want to invoke this command directly; it is
           meant to be used as a credential helper by other parts of git. See
           gitcredentials(7) or EXAMPLES below.

## [](#OPTIONS)OPTIONS

           --file=<path>
               Use <path> to lookup and store credentials. The file will have
               its filesystem permissions set to prevent other users on the
               system from reading it, but it will not be encrypted or
               otherwise protected. If not specified, credentials will be
               searched for from ~/.git-credentials and
               $XDG_CONFIG_HOME/git/credentials, and credentials will be
               written to ~/.git-credentials if it exists, or
               $XDG_CONFIG_HOME/git/credentials if it exists and the former
               does not. See also the section called “FILES”.

## [](#FILES)FILES

           If not set explicitly with --file, there are two files where
           git-credential-store will search for credentials in order of
           precedence:

           ~/.git-credentials
               User-specific credentials file.

           $XDG_CONFIG_HOME/git/credentials
               Second user-specific credentials file. If $XDG_CONFIG_HOME is
               not set or empty, $HOME/.config/git/credentials will be used.
               Any credentials stored in this file will not be used if
               ~/.git-credentials has a matching credential as well. It is a
               good idea not to create this file if you sometimes use older
               versions of Git that do not support it.

           For credential lookups, the files are read in the order given
           above, with the first matching credential found taking precedence
           over credentials found in files further down the list.

           Credential storage will by default write to the first existing
           file in the list. If none of these files exist, ~/.git-credentials
           will be created and written to.

           When erasing credentials, matching credentials will be erased from
           all files.

## [](#EXAMPLES)EXAMPLES

           The point of this helper is to reduce the number of times you must
           type your username or password. For example:

               $ git config credential.helper store
               $ git push http://example.com/repo.git
               Username: <type your username>
               Password: <type your password>

               [several days later]
               $ git push http://example.com/repo.git
               [your credentials are used automatically]

## [](#STORAGE_FORMAT)STORAGE FORMAT

           The .git-credentials file is stored in plaintext. Each credential
           is stored on its own line as a URL like:

               https://user:pass@example.com

           No other kinds of lines (e.g. empty lines or comment lines) are
           allowed in the file, even though some may be silently ignored. Do
           not view or edit the file with editors.

           When Git needs authentication for a particular URL context,
           credential-store will consider that context a pattern to match
           against each entry in the credentials file. If the protocol,
           hostname, and username (if we already have one) match, then the
           password is returned to Git. See the discussion of configuration
           in gitcredentials(7) for more information.

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

    Git 2.55.0.493.g5b2471          2026-08-03        GIT-CREDENTIAL-STORE(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [gitcredentials(7)](../man7/gitcredentials.7.html)

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
