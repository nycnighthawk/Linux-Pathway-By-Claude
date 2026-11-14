---
{"title": "dpkg-fsys-usrunmess(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dpkg-fsys-usrunmess.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dpkg-fsys-usrunmess(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [ENVIRONMENT](#ENVIRONMENT) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                               |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    dpkg-fsys-usrunmess(8)          dpkg suite         dpkg-fsys-usrunmess(8)

## [](#NAME)NAME

           dpkg-fsys-usrunmess - undoes the merged-/usr-via-aliased-dirs mess

## [](#SYNOPSIS)SYNOPSIS

           dpkg-fsys-usrunmess [option...]

## [](#DESCRIPTION)DESCRIPTION

           dpkg-fsys-usrunmess is a tool to fix up filesystems that have been
           installed anew with recent installers with unfortunate defaults or
           migrated to the broken merged /usr via aliased directories layout,
           which is not supported by dpkg.  See the dpkg FAQ.

           Note: In Debian its tech-ctte has decreed that on the release
           after bookworm the non-usrmerged layout is not going to be
           supported, and thus some of its maintainers might not fix issues
           or intentionally remove non-usrmerged support, so you will need
           decide and pick your poison.

           The program will perform the following overall actions:

           •   Check whether the system needs to be switched, otherwise do
               nothing,

           •   Check for dpkg database consistency and otherwise abort.

           •   Generate and install a regression prevention package, if
               requested on the command-line or otherwise on the prompt.

           •   Get the list of files and alternatives that need to be
               restored.

           •   Look for untracked kernel modules files that need to be moved
               too.

           •   Create a shadow hierarchy under /.usrunmess, by creating the
               directories symlinks or hardlinking or copying the files as
               needed.

           •   Prompt for confirmation before proceeding, if requested on the
               command-line.

           •   Lock the dpkg database.

           •   Mark all packages as half-configured to force running
               maintainer scripts that might need to recreate files.

           •   Replace the aliased directories with the shadow ones, by
               creating a backup of the old symlinked directories and
               renaming the shadow ones over.

           •   Relabel MAC information for directories and symlinks if
               necessary.

           •   Remove backup symlinks.

           •   Remove old moved objects, but defer directory removal.

           •   Remove old deferred directories that are not referenced by
               dpkg-query.

           •   Remove shadow root directory.

           •   Register a policy-rc.d to disallow service actions, which
               means that services might need to be restarted afterwards,
               ideally via a reboot.

           •   Reconfigure all packages.

           •   Unregister the policy-rc.d and restore the alternatives state.

           Note: When running the program from some shells such as bash(1) or
           zsh(1), after executing it, you might need to request the shell to
           forget all remembered executable locations with for example "hash
           -r".

           Note: Some directories might linger after the migration in case
           they contain untracked files.  A list is printed once the script
           has finished for further investigation.

           Warning: Note that this operation has the potential to render the
           system unusable or broken in case of a sudden crash or reboot,
           unexpected state of the system, or possible bugs in the script.
           Be prepared with recovery media and consider doing backups
           beforehand.

           This program was introduced in dpkg 1.20.6.

## [](#OPTIONS)OPTIONS

           -p, --prompt
               Prompt at the time of no return, so that the debug output or
               the shadow hierarchy can be evaluated before proceeding.

           --prevention
           --no-prevention
               Enables or disables generating and installing a regression
               prevention package into the system.  If no option has been
               specified, the action to take will be prompted.

               The generated package contains the Protected field set to yes
               to protect against accidental removal of the package.

           -n, --no-act
           --dry-run
               This option enables the dry-run mode, where no destructive
               action takes place, only the preparatory part.

           -?, --help
               Show the usage message and exit.

           --version
               Show the version and exit.

## [](#ENVIRONMENT)ENVIRONMENT

           DPKG_USRUNMESS_NOACT
               This setting defines whether to enable dry-run mode.

## [](#SEE_ALSO)SEE ALSO

           <https://wiki.debian.org/Teams/Dpkg/FAQ#broken-usrmerge>.

## [](#COLOPHON)COLOPHON

           This page is part of the dpkg (Debian Package Manager) project.
           Information about the project can be found at 
           ⟨https://wiki.debian.org/Teams/Dpkg/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://bugs.debian.org/cgi-bin/pkgreport.cgi?src=dpkg⟩.  This
           page was obtained from the project's upstream Git repository ⟨git
           clone https://git.dpkg.org/git/dpkg/dpkg.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.22.6-77-g86fe7                2024-03-10         dpkg-fsys-usrunmess(8)

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
