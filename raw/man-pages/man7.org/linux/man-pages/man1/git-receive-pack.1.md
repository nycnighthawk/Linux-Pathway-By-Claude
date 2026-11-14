---
{"title": "git-receive-pack(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-receive-pack.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-receive-pack(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [PRE-RECEIVE HOOK](#PRE-RECEIVE_HOOK) \| [UPDATE HOOK](#UPDATE_HOOK) \| [POST-RECEIVE HOOK](#POST-RECEIVE_HOOK) \| [POST-UPDATE HOOK](#POST-UPDATE_HOOK) \| [QUARANTINE ENVIRONMENT](#QUARANTINE_ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GIT-RECEIVE-PACK(1)             Git Manual            GIT-RECEIVE-PACK(1)

## [](#NAME)NAME

           git-receive-pack - Receive what is pushed into the repository

## [](#SYNOPSIS)SYNOPSIS

           git receive-pack <git-dir>

## [](#DESCRIPTION)DESCRIPTION

           Invoked by git send-pack and updates the repository with the
           information fed from the remote end.

           This command is usually not invoked directly by the end user. The
           UI for the protocol is on the git send-pack side, and the program
           pair is meant to be used to push updates to a remote repository.
           For pull operations, see git-fetch-pack(1).

           The command allows for the creation and fast-forwarding of sha1
           refs (heads/tags) on the remote end (strictly speaking, it is the
           local end git-receive-pack runs, but to the user who is sitting at
           the send-pack end, it is updating the remote. Confused?)

           There are other real-world examples of using update and
           post-update hooks found in the Documentation/howto directory.

           git-receive-pack honours the receive.denyNonFastForwards config
           option, which tells it if updates to a ref should be denied if
           they are not fast-forwards.

           A number of other receive.* config options are available to tweak
           its behavior, see git-config(1).

## [](#OPTIONS)OPTIONS

           <git-dir>
               The repository to sync into.

           --http-backend-info-refs
               Used by git-http-backend(1) to serve up
               $GIT_URL/info/refs?service=git-receive-pack requests. See
               --http-backend-info-refs in git-upload-pack(1).

           --skip-connectivity-check
               Bypasses the connectivity checks that validate the existence
               of all objects in the transitive closure of reachable objects.
               This option is intended for server operators that want to
               implement their own object connectivity validation outside of
               Git. This is useful in such cases where the server-side knows
               additional information about how Git is being used and thus
               can rely on certain guarantees to more efficiently compute
               object connectivity that Git itself cannot make. Usage of this
               option without a reliable external mechanism to ensure full
               reachable object connectivity risks corrupting the repository
               and should not be used in the general case.

## [](#PRE-RECEIVE_HOOK)PRE-RECEIVE HOOK

           Before any ref is updated, if $GIT_DIR/hooks/pre-receive file
           exists and is executable, it will be invoked once with no
           parameters. The standard input of the hook will be one line per
           ref to be updated:

               sha1-old SP sha1-new SP refname LF

           The refname value is relative to $GIT_DIR; e.g. for the master
           head this is "refs/heads/master". The two sha1 values before each
           refname are the object names for the refname before and after the
           update. Refs to be created will have sha1-old equal to 0{40},
           while refs to be deleted will have sha1-new equal to 0{40},
           otherwise sha1-old and sha1-new should be valid objects in the
           repository.

           When accepting a signed push (see git-push(1)), the signed push
           certificate is stored in a blob and an environment variable
           GIT_PUSH_CERT can be consulted for its object name. See the
           description of post-receive hook for an example. In addition, the
           certificate is verified using GPG and the result is exported with
           the following environment variables:

           GIT_PUSH_CERT_SIGNER
               The name and the e-mail address of the owner of the key that
               signed the push certificate.

           GIT_PUSH_CERT_KEY
               The GPG key ID of the key that signed the push certificate.

           GIT_PUSH_CERT_STATUS
               The status of GPG verification of the push certificate, using
               the same mnemonic as used in %G? format of git log family of
               commands (see git-log(1)).

           GIT_PUSH_CERT_NONCE
               The nonce string the process asked the signer to include in
               the push certificate. If this does not match the value
               recorded on the "nonce" header in the push certificate, it may
               indicate that the certificate is a valid one that is being
               replayed from a separate "git push" session.

           GIT_PUSH_CERT_NONCE_STATUS

               UNSOLICITED
                   "git push --signed" sent a nonce when we did not ask it to
                   send one.

               MISSING
                   "git push --signed" did not send any nonce header.

               BAD
                   "git push --signed" sent a bogus nonce.

               OK
                   "git push --signed" sent the nonce we asked it to send.

               SLOP
                   "git push --signed" sent a nonce different from what we
                   asked it to send now, but in a previous session. See
                   GIT_PUSH_CERT_NONCE_SLOP environment variable.

           GIT_PUSH_CERT_NONCE_SLOP
               "git push --signed" sent a nonce different from what we asked
               it to send now, but in a different session whose starting time
               is different by this many seconds from the current session.
               Only meaningful when GIT_PUSH_CERT_NONCE_STATUS says SLOP.
               Also read about receive.certNonceSlop variable in
               git-config(1).

           This hook is called before any refname is updated and before any
           fast-forward checks are performed.

           If the pre-receive hook exits with a non-zero exit status no
           updates will be performed, and the update, post-receive and
           post-update hooks will not be invoked either. This can be useful
           to quickly bail out if the update is not to be supported.

           See the notes on the quarantine environment below.

## [](#UPDATE_HOOK)UPDATE HOOK

           Before each ref is updated, if $GIT_DIR/hooks/update file exists
           and is executable, it is invoked once per ref, with three
           parameters:

               $GIT_DIR/hooks/update refname sha1-old sha1-new

           The refname parameter is relative to $GIT_DIR; e.g. for the master
           head this is "refs/heads/master". The two sha1 arguments are the
           object names for the refname before and after the update. Note
           that the hook is called before the refname is updated, so either
           sha1-old is 0{40} (meaning there is no such ref yet), or it should
           match what is recorded in refname.

           The hook should exit with non-zero status if it wants to disallow
           updating the named ref. Otherwise it should exit with zero.

           Successful execution (a zero exit status) of this hook does not
           ensure the ref will actually be updated, it is only a
           prerequisite. As such it is not a good idea to send notices (e.g.
           email) from this hook. Consider using the post-receive hook
           instead.

## [](#POST-RECEIVE_HOOK)POST-RECEIVE HOOK

           After all refs were updated (or attempted to be updated), if any
           ref update was successful, and if $GIT_DIR/hooks/post-receive file
           exists and is executable, it will be invoked once with no
           parameters. The standard input of the hook will be one line for
           each successfully updated ref:

               sha1-old SP sha1-new SP refname LF

           The refname value is relative to $GIT_DIR; e.g. for the master
           head this is "refs/heads/master". The two sha1 values before each
           refname are the object names for the refname before and after the
           update. Refs that were created will have sha1-old equal to 0{40},
           while refs that were deleted will have sha1-new equal to 0{40},
           otherwise sha1-old and sha1-new should be valid objects in the
           repository.

           The GIT_PUSH_CERT* environment variables can be inspected, just as
           in pre-receive hook, after accepting a signed push.

           Using this hook, it is easy to generate mails describing the
           updates to the repository. This example script sends one mail
           message per ref listing the commits pushed to the repository, and
           logs the push certificates of signed pushes with good signatures
           to a logger service:

               #!/bin/sh
               # mail out commit update information.
               while read oval nval ref
               do
                       if expr "$oval" : '0*$' >/dev/null
                       then
                               echo "Created a new ref, with the following commits:"
                               git rev-list --pretty "$nval"
                       else
                               echo "New commits:"
                               git rev-list --pretty "$nval" "^$oval"
                       fi |
                       mail -s "Changes to ref $ref" commit-list@mydomain
               done
               # log signed push certificate, if any
               if test -n "${GIT_PUSH_CERT-}" && test ${GIT_PUSH_CERT_STATUS} = G
               then
                       (
                               echo expected nonce is ${GIT_PUSH_NONCE}
                               git cat-file blob ${GIT_PUSH_CERT}
                       ) | mail -s "push certificate from $GIT_PUSH_CERT_SIGNER" push-log@mydomain
               fi
               exit 0

           The exit code from this hook invocation is ignored, however a
           non-zero exit code will generate an error message.

           Note that it is possible for refname to not have sha1-new when
           this hook runs. This can easily occur if another user modifies the
           ref after it was updated by git-receive-pack, but before the hook
           was able to evaluate it. It is recommended that hooks rely on
           sha1-new rather than the current value of refname.

## [](#POST-UPDATE_HOOK)POST-UPDATE HOOK

           After all other processing, if at least one ref was updated, and
           if $GIT_DIR/hooks/post-update file exists and is executable, then
           post-update will be called with the list of refs that have been
           updated. This can be used to implement any repository wide cleanup
           tasks.

           The exit code from this hook invocation is ignored; the only thing
           left for git-receive-pack to do at that point is to exit itself
           anyway.

           This hook can be used, for example, to run git update-server-info
           if the repository is packed and is served via a dumb transport.

               #!/bin/sh
               exec git update-server-info

## [](#QUARANTINE_ENVIRONMENT)QUARANTINE ENVIRONMENT

           When receive-pack takes in objects, they are placed into a
           temporary "quarantine" directory within the $GIT_DIR/objects
           directory and migrated into the main object store only after the
           pre-receive hook has completed. If the push fails before then, the
           temporary directory is removed entirely.

           This has a few user-visible effects and caveats:

            1. Pushes which fail due to problems with the incoming pack,
               missing objects, or due to the pre-receive hook will not leave
               any on-disk data. This is usually helpful to prevent repeated
               failed pushes from filling up your disk, but can make
               debugging more challenging.

            2. Any objects created by the pre-receive hook will be created in
               the quarantine directory (and migrated only if it succeeds).

            3. The pre-receive hook MUST NOT update any refs to point to
               quarantined objects. Other programs accessing the repository
               will not be able to see the objects (and if the pre-receive
               hook fails, those refs would become corrupted). For safety,
               any ref updates from within pre-receive are automatically
               rejected.

## [](#SEE_ALSO)SEE ALSO

           git-send-pack(1), gitnamespaces(7)

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

    Git 2.55.0.493.g5b2471          2026-08-03            GIT-RECEIVE-PACK(1)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-config(1)](../man1/git-config.1.html),  [git-push(1)](../man1/git-push.1.html),  [git-send-pack(1)](../man1/git-send-pack.1.html),  [git-upload-pack(1)](../man1/git-upload-pack.1.html),  [githooks(5)](../man5/githooks.5.html),  [gitnamespaces(7)](../man7/gitnamespaces.7.html)

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
