---
{"title": "gitcvs-migration(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/gitcvs-migration.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# gitcvs-migration(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DEVELOPING AGAINST A SHARED REPOSITORY](#DEVELOPING_AGAINST_A_SHARED_REPOSITORY) \| [SETTING UP A SHARED REPOSITORY](#SETTING_UP_A_SHARED_REPOSITORY) \| [IMPORTING A CVS ARCHIVE](#IMPORTING_A_CVS_ARCHIVE) \| [ADVANCED SHARED REPOSITORY MANAGEMENT](#ADVANCED_SHARED_REPOSITORY_MANAGEMENT) \| [PROVIDING CVS ACCESS TO A GIT REPOSITORY](#PROVIDING_CVS_ACCESS_TO_A_GIT_REPOSITORY) \| [ALTERNATIVE DEVELOPMENT MODELS](#ALTERNATIVE_DEVELOPMENT_MODELS) \| [SEE ALSO](#SEE_ALSO) \| [GIT](#GIT) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    GITCVS-MIGRATION(7)             Git Manual            GITCVS-MIGRATION(7)

## [](#NAME)NAME

           gitcvs-migration - Git for CVS users

## [](#SYNOPSIS)SYNOPSIS

           git cvsimport *

## [](#DESCRIPTION)DESCRIPTION

           Git differs from CVS in that every working tree contains a
           repository with a full copy of the project history, and no
           repository is inherently more important than any other. However,
           you can emulate the CVS model by designating a single shared
           repository which people can synchronize with; this document
           explains how to do that.

           Some basic familiarity with Git is required. Having gone through
           gittutorial(7) and gitglossary(7) should be sufficient.

## [](#DEVELOPING_AGAINST_A_SHARED_REPOSITORY)DEVELOPING AGAINST A SHARED REPOSITORY

           Suppose a shared repository is set up in /pub/repo.git on the host
           foo.com. Then as an individual committer you can clone the shared
           repository over ssh with:

               $ git clone foo.com:/pub/repo.git/ my-project
               $ cd my-project

           and hack away. The equivalent of cvs update is

               $ git pull origin

           which merges in any work that others might have done since the
           clone operation. If there are uncommitted changes in your working
           tree, commit them first before running git pull.

               Note

               The pull command knows where to get updates from because of
               certain configuration variables that were set by the first git
               clone command; see the subcommand list in git-config(1) for
               details.

           You can update the shared repository with your changes by first
           committing your changes, and then using the git push command:

               $ git push origin master

           to "push" those commits to the shared repository. If someone else
           has updated the repository more recently, git push, like cvs
           commit, will complain, in which case you must pull any changes
           before attempting the push again.

           In the git push command above we specify the name of the remote
           branch to update (master). If we leave that out, git push tries to
           update any branches in the remote repository that have the same
           name as a branch in the local repository. So the last push can be
           done with either of:

               $ git push origin
               $ git push foo.com:/pub/project.git/

           as long as the shared repository does not have any branches other
           than master.

## [](#SETTING_UP_A_SHARED_REPOSITORY)SETTING UP A SHARED REPOSITORY

           We assume you have already created a Git repository for your
           project, possibly created from scratch or from a tarball (see
           gittutorial(7)), or imported from an already existing CVS
           repository (see the next section).

           Assume your existing repo is at /home/alice/myproject. Create a
           new "bare" repository (a repository without a working tree) and
           fetch your project into it:

               $ mkdir /pub/my-repo.git
               $ cd /pub/my-repo.git
               $ git --bare init --shared
               $ git --bare fetch /home/alice/myproject master:master

           Next, give every team member read/write access to this repository.
           One easy way to do this is to give all the team members ssh access
           to the machine where the repository is hosted. If you don’t want
           to give them a full shell on the machine, there is a restricted
           shell which only allows users to do Git pushes and pulls; see
           git-shell(1).

           Put all the committers in the same group, and make the repository
           writable by that group:

               $ chgrp -R $group /pub/my-repo.git

           Make sure committers have a umask of at most 027, so that the
           directories they create are writable and searchable by other group
           members.

## [](#IMPORTING_A_CVS_ARCHIVE)IMPORTING A CVS ARCHIVE

               Note

               These instructions use the git-cvsimport script which ships
               with git, but other importers may provide better results. See
               the note in git-cvsimport(1) for other options.

           First, install version 2.1 or higher of cvsps from
           https://github.com/andreyvit/cvsps and make sure it is in your
           path. Then cd to a checked out CVS working directory of the
           project you are interested in and run git-cvsimport(1):

               $ git cvsimport -C <destination> <module>

           This puts a Git archive of the named CVS module in the directory
           <destination>, which will be created if necessary.

           The import checks out from CVS every revision of every file.
           Reportedly cvsimport can average some twenty revisions per second,
           so for a medium-sized project this should not take more than a
           couple of minutes. Larger projects or remote repositories may take
           longer.

           The main trunk is stored in the Git branch named origin, and
           additional CVS branches are stored in Git branches with the same
           names. The most recent version of the main trunk is also left
           checked out on the master branch, so you can start adding your own
           changes right away.

           The import is incremental, so if you call it again next month it
           will fetch any CVS updates that have been made in the meantime.
           For this to work, you must not modify the imported branches;
           instead, create new branches for your own changes, and merge in
           the imported branches as necessary.

           If you want a shared repository, you will need to make a bare
           clone of the imported directory, as described above. Then treat
           the imported directory as another development clone for purposes
           of merging incremental imports.

## [](#ADVANCED_SHARED_REPOSITORY_MANAGEMENT)ADVANCED SHARED REPOSITORY MANAGEMENT

           Git allows you to specify scripts called "hooks" to be run at
           certain points. You can use these, for example, to send all
           commits to the shared repository to a mailing list. See
           githooks(5).

           You can enforce finer grained permissions using update hooks. See
           Controlling access to branches using update hooks[1].

## [](#PROVIDING_CVS_ACCESS_TO_A_GIT_REPOSITORY)PROVIDING CVS ACCESS TO A GIT REPOSITORY

           It is also possible to provide true CVS access to a Git
           repository, so that developers can still use CVS; see
           git-cvsserver(1) for details.

## [](#ALTERNATIVE_DEVELOPMENT_MODELS)ALTERNATIVE DEVELOPMENT MODELS

           CVS users are accustomed to giving a group of developers commit
           access to a common repository. As we’ve seen, this is also
           possible with Git. However, the distributed nature of Git allows
           other development models, and you may want to first consider
           whether one of them might be a better fit for your project.

           For example, you can choose a single person to maintain the
           project’s primary public repository. Other developers then clone
           this repository and each work in their own clone. When they have a
           series of changes that they’re happy with, they ask the maintainer
           to pull from the branch containing the changes. The maintainer
           reviews their changes and pulls them into the primary repository,
           which other developers pull from as necessary to stay coordinated.
           The Linux kernel and other projects use variants of this model.

           With a small group, developers may just pull changes from each
           other’s repositories without the need for a central maintainer.

## [](#SEE_ALSO)SEE ALSO

           gittutorial(7), gittutorial-2(7), gitcore-tutorial(7),
           gitglossary(7), giteveryday(7), The Git User’s Manual[2]

## [](#GIT)GIT

           Part of the git(1) suite

## [](#NOTES)NOTES

            1. Controlling access to branches using update hooks
               file:///home/mtk/share/doc/git-doc/howto/update-hook-example.html

            2. The Git User’s Manual
               file:///home/mtk/share/doc/git-doc/user-manual.html

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

    Git 2.55.0.493.g5b2471          2026-08-03            GITCVS-MIGRATION(7)

------------------------------------------------------------------------

Pages that refer to this page: [git(1)](../man1/git.1.html),  [git-cvsimport(1)](../man1/git-cvsimport.1.html),  [git-cvsserver(1)](../man1/git-cvsserver.1.html),  [gitcore-tutorial(7)](../man7/gitcore-tutorial.7.html),  [gitglossary(7)](../man7/gitglossary.7.html),  [gittutorial-2(7)](../man7/gittutorial-2.7.html),  [gittutorial(7)](../man7/gittutorial.7.html)

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
