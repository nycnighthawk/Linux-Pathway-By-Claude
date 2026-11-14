---
{"title": "pstree(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/pstree.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pstree(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [FILES](#FILES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                    |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PSTREE(1)                     User Commands                     PSTREE(1)

## [](#NAME)NAME

           pstree - display a tree of processes

## [](#SYNOPSIS)SYNOPSIS

           pstree [option ...] [pid , user]

## [](#DESCRIPTION)DESCRIPTION

           pstree shows running processes as a tree.  The tree is rooted at
           either pid or init if pid is omitted.  If a user name is
           specified, all process trees rooted at processes owned by that
           user are shown.

           pstree visually merges identical branches by putting them in
           square brackets and prefixing them with the repetition count, e.g.

               init-+-getty
                    |-getty
                    |-getty
                    `-getty

           becomes

               init---4*[getty]

           Child threads of a process are found under the parent process and
           are shown with the process name in curly braces, e.g.

               icecast2---13*[{icecast2}]

           If pstree is called as pstree.x11 then it will prompt the user at
           the end of the line to press return and will not return until that
           has happened.  This is useful for when pstree is run in a
           xterminal.

           Certain kernel or mount parameters, such as the hidepid option for
           procfs, will hide information for some processes. In these
           situations pstree will attempt to build the tree without this
           information, showing process names as question marks.

## [](#OPTIONS)OPTIONS

           -a, --arguments
                  Show command line arguments.  If the command line of a
                  process is swapped out, that process is shown in
                  parentheses.  -a implicitly disables compaction for
                  processes but not threads.

           -A, --ascii
                  Use ASCII characters to draw the tree.

           -c, --compact-not
                  Disable compaction of identical subtrees.  By default,
                  subtrees are compacted whenever possible.

           -C, --color=TYPE
                  Color the process name by given attribute. Currently pstree
                  only accepts the value age which colors by process age.
                  Processes newer than 60 seconds are green, newer than an
                  hour yellow and the remaining red.

           -g, --show-pgids
                  Show PGIDs.  Process Group IDs are shown as decimal numbers
                  in parentheses after each process name.  If both PIDs and
                  PGIDs are displayed then PIDs are shown first.

           -G, --vt100
                  Use VT100 line drawing characters.

           -h, --hightlight-all
                  Highlight the current process and its ancestors.  This is a
                  no-op if the terminal doesn't support highlighting or if
                  neither the current process nor any of its ancestors are in
                  the subtree being shown.

           -H, --highlight-pid=PID
                  Like -h, but highlight the specified process instead.
                  Unlike with -h, pstree fails when using -H if highlighting
                  is not available.

           -k, --kthreads
                  Show kernel threads.

           -l, --long
                  Display long lines.  By default, lines are truncated to
                  either the COLUMNS environment variable or the display
                  width.  If neither of these methods work, the default of
                  132 columns is used.

           -n, --numeric-sort
                  Sort processes with the same parent by PID instead of by
                  name.  (Numeric sort.)

           -N, --ns-sort=TYPE
                  Show individual trees for each namespace of TYPE.  The
                  available types are: ipc, mnt, net, pid, time, user, uts.
                  Regular users don't have access to other users' processes
                  information, so the output will be limited.

           -p, --show-pids
                  Show PIDs.  PIDs are shown as decimal numbers in
                  parentheses after each process name.  -p implicitly
                  disables compaction.

           -P --show-paths
                  Show the full path to the running process on disk.

           -s, --show-parents
                  Show parent processes of the specified process.

           -S, --ns-changes
                  Show namespaces transitions.  Like -N, the output is
                  limited when running as a regular user.

           -t, --thread-names
                  Show full names for threads when available.

           -T, --hide-threads
                  Hide threads and only show processes.

           -u, --uid-changes
                  Show uid transitions.  Whenever the uid of a process
                  differs from the uid of its parent, the new uid is shown in
                  parentheses after the process name.

           -U, --unicode
                  Use UTF-8 (Unicode) line drawing characters.  Under Linux
                  1.1-54 and above, UTF-8 mode is entered on the console with
                  echo -e ' 33%8' and left with echo -e ' 33%@'.

           -V, --version
                  Display version information.

           -Z, --security-context
                  Show the current security attributes of the process. For
                  SELinux systems this will be the security context.

## [](#FILES)FILES

           /proc  location of the proc file system

## [](#BUGS)BUGS

           Some character sets may be incompatible with the VT100 characters.

## [](#SEE_ALSO)SEE ALSO

           ps(1), top(1), proc(5).

## [](#COLOPHON)COLOPHON

           This page is part of the psmisc (Small utilities that use the
           /proc filesystem) project.  Information about the project can be
           found at ⟨https://gitlab.com/psmisc/psmisc⟩.  If you have a bug
           report for this manual page, see
           ⟨https://gitlab.com/psmisc/psmisc/issues⟩.  This page was obtained
           from the project's upstream Git repository
           ⟨https://gitlab.com/psmisc/psmisc.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2025-10-21.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    psmisc                          2025-10-21                      PSTREE(1)

------------------------------------------------------------------------

Pages that refer to this page: [ps(1)](../man1/ps.1.html),  [proc(5)](../man5/proc.5.html)

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
