---
{"title": "git-series(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/git-series.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# git-series(1) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SUBCOMMANDS](#SUBCOMMANDS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                        |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    git-series(1)            General Commands Manual            git-series(1)

## [](#NAME)NAME

           git-series - track changes to a patch series with git

## [](#SYNOPSIS)SYNOPSIS

           git series [SUBCOMMAND] [OPTIONS]

## [](#DESCRIPTION)DESCRIPTION

           git series tracks changes to a patch series over time.  git series
           also tracks a cover letter for the patch series, formats the
           series for email, and prepares pull requests.

           Use git series start seriesname to start a patch series
           seriesname.  Use normal git commands to commit changes, and use
           git series status to check what has changed.  Use git series cover
           to add or edit a cover letter.  Use git series add and git series
           commit (or git series commit -a) to commit changes to the patch
           series.  Use git series rebase -i to help rework or reorganize the
           patch series.  Use git series format to prepare the patch series
           to send via email, or git series req to prepare a "please pull"
           mail.

           Running git series without arguments shows the list of patch
           series, marking the current patch series with a '*'.

## [](#SUBCOMMANDS)SUBCOMMANDS

           git series add change...
                  Add changes to the staging area for the next git series
                  commit.

                  change...
                         Changes to add: any combination of "series", "base",
                         and "cover".

           git series base [-d|--delete] [base]
                  Get or set the base commit for the patch series.  With no
                  parameters, print the hash of the base commit.  With
                  parameters, set or delete the base commit.

                  This only changes the base in the working version of the
                  patch series; use git series add base to add that change to
                  the next git series commit, or use git series commit -a to
                  commit the new base and all other changes to the series in
                  one step.

                  base   New base commit.  This can use a commit hash, ref
                         name, or special syntaxes such as refname^ or
                         refname~2.

                  -d|--delete
                         Delete the current base commit.

           git series checkout name
                  Resume work on the patch series name; check out the current
                  version as HEAD.

           git series commit [-a|--all] [-m message] [-v|--verbose]
                  Record a new version of the patch series.  Without
                  arguments, this will run an editor to edit a commit
                  message, and then commit the changes previously added with
                  git series add.

                  -a|--all
                         Commit all changes, not just those added with git
                         series add.

                  -m message
                         Use message as the commit message, rather than
                         running an editor.

                  -v|--verbose
                         Show a diff of the commit in the editor, below the
                         commit message, as a reminder of the changes in the
                         commit.  This diff will not appear in the commit
                         message.

           git series cover [-d|--delete]
                  Create or edit the cover letter for the patch series.
                  Without arguments, this will run an editor to edit the
                  cover letter.

                  This only changes the cover letter in the working version
                  of the patch series; use git series add cover to add that
                  change to the next git series commit, or use git series
                  commit -a to commit the new cover letter and all other
                  changes to the series in one step.

                  -d|--delete
                         Delete the cover letter rather than editing it.

           git series cp [source] dest
                  Copy the series source to dest, including any work in
                  progress, staged or unstaged.  source defaults to the
                  current series if omitted.

           git series delete name
                  Delete the series name, including any work in progress,
                  staged or unstaged.

           git series detach
                  Stop working on any patch series.  Any changes in progress,
                  staged or unstaged, will remain intact.  To start working
                  on the branch again, use git series checkout.

           git series diff
                  Show changes to the patch series from the current working
                  version to the staged version.  Changes to the cover letter
                  appear as standard text diffs.  If both the old and new
                  version contain base and series entries, git series diff
                  will find and show the correspondence between the old and
                  new versions of each commit.  The series diff format shows
                  reordered commits, deleted or added commits, and modified
                  commits.  For modified commits, the series diff includes a
                  simplified interdiff between the commits.

           git series format [--in-reply-to=Message-Id] [--no-from] [-v N |
           --reroll-count=N] [--rfc] [--stdout] [--subject-prefix=prefix]
                  Prepare the patch series to send via email.  This creates
                  one file per patch in the series, plus one additional file
                  for the cover letter if any.  The patch series must have a
                  base set with git series base, to identify the series of
                  patches to format.

                  Each file contains one email in mbox format, ready to send,
                  with email headers threading all the patches together.  If
                  the series has a cover letter, all of the patches will
                  include headers to make them a reply to the cover letter;
                  otherwise, all of the patches will include headers to make
                  them a reply to the first patch.

                  --in-reply-to=Message-Id
                         Make the first mail a reply to the specified
                         Message-Id.  The Message-Id may include or omit the
                         surrounding angle brackets; git-series will add them
                         if not present.

                  --no-from
                         By default, git series format includes a "From:"
                         line in the mail body for the commit author when
                         formatting commits you didn't write; this allows you
                         to send the patches as emails from your own address
                         while preserving authorship information for each
                         patch.  git series format --no-from will instead use
                         the commit author as the "From:" address for each
                         patch mail.  Use this when producing patch files for
                         purposes other than email.

                  -v N | --reroll-count=N
                         Mark the patch series as PATCH vN.  The patch
                         filenames and mail subjects will include the version
                         number.

                  --rfc  Use [RFC PATCH] instead of the standard [PATCH]
                         prefix.

                  --stdout
                         Write the entire patch series to stdout rather than
                         to separate patch files.

                  --subject-prefix=prefix
                         Use [prefix] instead of the standard [PATCH] prefix.

           git series help [subcommand]
                  Show help for git series or a subcommand.  Without
                  arguments, shows a summary of the subcommands supported by
                  git series.

                  subcommand
                         Show help for subcommand.

           git series log [-p|--patch]
                  Show the history of the patch series.

                  -p|--patch
                         Include a patch for each change committed to the
                         series.  This uses the same series diff format as
                         git series diff.

           git series mv [source] dest
                  Move (rename) the series source to dest, including any work
                  in progress, staged or unstaged.  source defaults to the
                  current series if omitted.  Moving the current series will
                  make the destination the current series.

                  You can also invoke this as git series rename.

           git series rebase [-i|--interactive] [onto]
                  Rebase the patch series, either onto a new base,
                  interactively, or both.  The patch series must have a base
                  set with git series base, to identify the series of patches
                  to rebase.

                  onto   Commit to rebase the series onto.  This can use a
                         commit hash, ref name, or special syntaxes such as
                         refname^ or refname~2.

                  -i|--interactive
                         Interactively edit the list of commits.  This uses
                         the same format and syntax as git rebase -i, to
                         allow reordering, dropping, combining, or editing
                         commits.

           git series req [-p|--patch] url tag
                  Generate a mail requesting a pull of the patch series.

                  Before running this command, push the patch series to the
                  repository at url, as a tag or branch named tag.

                  A pull request for a signed or annotated tag will include
                  the message from the tag.  The pull request will also
                  include the cover letter if any, unless the tag message
                  already contains the cover letter.  The subject of the mail
                  will include the first line from the cover letter, or the
                  name of the series if no cover letter.

                  The patch series must have a base set with git series base,
                  to identify the series of patches to request a pull of.

                  url    URL of the repository to pull from.

                  tag    Name of a tag or branch to request a pull from.

                  -p|--patch
                         Include a patch showing the combined change made by
                         all the patches in the series.  This can help a
                         reviewer see the effect of pulling the series.

           git series start name
                  Start a new patch series named name.

           git series status
                  Show the status of the current patch series.

                  This shows any changes staged for the next git series
                  commit, changes in the current working copy but not staged
                  for the next git series commit, and hints about the next
                  commands to run.

           git series unadd change
                  Remove changes from the next git series commit, undoing git
                  series add.

                  The changes remain in the current working version of the
                  series.

                  change...
                         Changes to remove: any combination of "series",
                         "base", and "cover".

## [](#SEE_ALSO)SEE ALSO

           git(1)

## [](#COLOPHON)COLOPHON

           This page is part of the git-series (track changes to a Git patch
           series over time) project.  Information about the project can be
           found at ⟨https://github.com/git-series/git-series⟩.  If you have
           a bug report for this manual page, see
           ⟨https://github.com/git-series/git-series/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/git-series/git-series⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2024-02-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                                                git-series(1)

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
