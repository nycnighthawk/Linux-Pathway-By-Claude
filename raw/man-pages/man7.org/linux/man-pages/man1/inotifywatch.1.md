---
{"title": "inotifywatch(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/inotifywatch.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# inotifywatch(1) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OUTPUT](#OUTPUT) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EVENTS](#EVENTS) \| [EXAMPLE](#EXAMPLE) \| [CAVEATS](#CAVEATS) \| [BUGS](#BUGS) \| [AUTHORS](#AUTHORS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                                               |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    inotifywatch(1)          General Commands Manual          inotifywatch(1)

## [](#NAME)NAME

           inotifywatch, fsnotifywatch - gather filesystem access statistics
           using inotify or fanotify

## [](#SYNOPSIS)SYNOPSIS

           inotifywatch [-hvzrPqfIFS] [-e <event> ] [-t <seconds> ] [-a
           <event> ] [-d <event> ] <file> [ ... ]

           fsnotifywatch [-hvzrPqfIFS] [-e <event> ] [-t <seconds> ] [-a
           <event> ] [-d <event> ] <file> [ ... ]

## [](#DESCRIPTION)DESCRIPTION

           inotifywatch listens for filesystem events using Linux's
           inotify(7) interface by default, then outputs a summary count of
           the events received on each file or directory.

           fsnotifywatch is similar to inotifywatch but it is using Linux's
           fanotify(7) interface by default. If explicitly specified, it uses
           the inotify(7) interface.

## [](#OUTPUT)OUTPUT

           inotifywatch and fsnotifywatch will output a table on standard out
           with one column for each type of event and one row for each
           watched file or directory.  The table will show the amount of
           times each event occurred for each watched file or directory.
           Output can be sorted by a particular event using the -a or -d
           options.

           Some diagnostic information will be output on standard error.

## [](#OPTIONS)OPTIONS

           -h, --help
                  Output some helpful usage information.

           -v, --verbose
                  Output some extra information on standard error during
                  execution.

           @<file>
                  When watching a directory tree recursively, exclude the
                  specified file from being watched.  The file must be
                  specified with a relative or absolute path according to
                  whether a relative or absolute path is given for watched
                  directories.  If a specific path is explicitly both
                  included and excluded, it will always be watched.

                  Note: If you need to watch a directory or file whose name
                  starts with @, give the absolute path.

           --fromfile <file>
                  Read filenames to watch or exclude from a file, one
                  filename per line.  If filenames begin with @ they are
                  excluded as described above.  If <file> is `-', filenames
                  are read from standard input.  Use this option if you need
                  to watch too many files to pass in as command line
                  arguments.

           -z, --zero
                  Output table rows and columns even if all elements are
                  zero.  By default, rows and columns are only output if they
                  contain non-zero elements.  Using this option when watching
                  for every event on a lot of files can result in a lot of
                  output!

           --exclude <pattern>
                  Do not process any events for the subset of files whose
                  filenames match the specified POSIX regular expression,
                  case sensitive.

           --excludei <pattern>
                  Do not process any events for the subset of files whose
                  filenames match the specified POSIX regular expression,
                  case insensitive.

           --include <pattern>
                  Process events only for the subset of files whose filenames
                  match the specified POSIX regular expression, case
                  sensitive.

           --includei <pattern>
                  Process events only for the subset of files whose filenames
                  match the specified POSIX regular expression, case
                  insensitive.

           -r, --recursive
                  Watch all subdirectories of any directories passed as
                  arguments.  Watches will be set up recursively to an
                  unlimited depth.  Symbolic links are not traversed.  If new
                  directories are created within watched directories they
                  will automatically be watched.

                  Warning: If you use this option while watching the root
                  directory of a large tree, it may take quite a while until
                  all inotify watches are established, and events will not be
                  received in this time.  Also, since one inotify watch will
                  be established per subdirectory, it is possible that the
                  maximum amount of inotify watches per user will be reached.
                  The default maximum is 8192; it can be increased by writing
                  to /proc/sys/fs/inotify/max_user_watches.

           -P, --no-dereference
                  Do not follow symlinks.

           -t <seconds>, --timeout <seconds>
                  Listen only for the specified amount of seconds.  If not
                  specified, inotifywatch will gather statistics until
                  receiving an interrupt signal by (for example) pressing
                  CONTROL-C at the console.

           -e <event>, --event <event>
                  Listen for specific event(s) only.  The events which can be
                  listened for are listed in the EVENTS section.  This option
                  can be specified more than once.  If omitted, all events
                  are listened for.

           -a <event>, --ascending <event>
                  Sort output ascending by event counts for the specified
                  event.  Sortable events include `total' and all the events
                  listed in the EVENTS section except `move' and `close' (you
                  must use `moved_to', `moved_from', `close_write' or
                  `close_nowrite' instead).  The default is to sort
                  descending by `total'.

           -d <event>, --descending <event>
                  Sort output descending by event counts for the specified
                  event.  Sortable events include `total' and all the events
                  listed in the EVENTS section except `move' and `close' (you
                  must use `moved_to', `moved_from', `close_write' or
                  `close_nowrite' instead).  The default is to sort
                  descending by `total'.

           -I, --inotify
                  Watch using inotify (default for inotifywatch).

           -F, --fanotify
                  Watch using fanotify (default for fsnotifywatch).  fanotify
                  support for reporting events with inotify compatible
                  information was added in kernel v5.9.  With older kernels
                  the command will fail.  As of kernel v5.12, fanotify
                  requires admin privileges.

           -S, --filesystem
                  Watch entire filesystem of any directories passed as
                  arguments using fanotify.

## [](#EXIT_STATUS)EXIT STATUS

           0      The program executed successfully.

           1      An error occurred in execution of the program.

## [](#EVENTS)EVENTS

           The following events are valid for use with the -e option:

           access A watched file or a file within a watched directory was
                  read from.

           modify A watched file or a file within a watched directory was
                  written to.

           attrib The metadata of a watched file or a file within a watched
                  directory was modified.  This includes timestamps, file
                  permissions, extended attributes etc.

           close_write
                  A watched file or a file within a watched directory was
                  closed, after being opened in writable mode.  This does not
                  necessarily imply the file was written to.

           close_nowrite
                  A watched file or a file within a watched directory was
                  closed, after being opened in read-only mode.

           close  A watched file or a file within a watched directory was
                  closed, regardless of how it was opened.  Note that this is
                  actually implemented simply by listening for both
                  close_write and close_nowrite, hence all close events
                  received will be output as one of these, not CLOSE.

           open   A watched file or a file within a watched directory was
                  opened.

           moved_to
                  A file or directory was moved into a watched directory.
                  This event occurs even if the file is simply moved from and
                  to the same directory.

           moved_from
                  A file or directory was moved from a watched directory.
                  This event occurs even if the file is simply moved from and
                  to the same directory.

           move   A file or directory was moved from or to a watched
                  directory.  Note that this is actually implemented simply
                  by listening for both moved_to and moved_from, hence all
                  close events received will be output as one or both of
                  these, not MOVE.

           move_self
                  A watched file or directory was moved. After this event,
                  the file or directory is no longer being watched.

           create A file or directory was created within a watched directory.

           delete A file or directory within a watched directory was deleted.

           delete_self
                  A watched file or directory was deleted.  After this event
                  the file or directory is no longer being watched.  Note
                  that this event can occur even if it is not explicitly
                  being listened for.

           unmount
                  The filesystem on which a watched file or directory resides
                  was unmounted.  After this event the file or directory is
                  no longer being watched.  Note that this event can occur
                  even if it is not explicitly being listened to.

## [](#EXAMPLE)EXAMPLE

           Watching the `~/.beagle' directory for 60 seconds:

           % inotifywatch -v -e access -e modify -t 60 -r ~/.beagle
           Establishing watches...
           Setting up watch(es) on /home/rohan/.beagle
           OK, /home/rohan/.beagle is now being watched.
           Total of 302 watches.
           Finished establishing watches, now collecting statistics.
           Will listen for events for 60 seconds.
           total  access  modify  filename
           1436   1074    362     /home/rohan/.beagle/Indexes/FileSystemIndex/PrimaryIndex/
           1323   1053    270     /home/rohan/.beagle/Indexes/FileSystemIndex/SecondaryIndex/
           303    116     187     /home/rohan/.beagle/Indexes/KMailIndex/PrimaryIndex/
           261    74      187     /home/rohan/.beagle/TextCache/
           206    0       206     /home/rohan/.beagle/Log/
           42     0       42      /home/rohan/.beagle/Indexes/FileSystemIndex/Locks/
           18     6       12      /home/rohan/.beagle/Indexes/FileSystemIndex/
           12     0       12      /home/rohan/.beagle/Indexes/KMailIndex/Locks/
           3      0       3       /home/rohan/.beagle/TextCache/54/
           3      0       3       /home/rohan/.beagle/TextCache/bc/
           3      0       3       /home/rohan/.beagle/TextCache/20/
           3      0       3       /home/rohan/.beagle/TextCache/62/
           2      2       0       /home/rohan/.beagle/Indexes/KMailIndex/SecondaryIndex/

## [](#CAVEATS)CAVEATS

           When using inotifywatch, the filename that is outputted is not
           guaranteed to be up to date after a move because it is the inode
           that is being monitored. Additionally, none of the observed
           operations are guaranteed to have been performed on the filename
           inotifywatch was instructed to monitor in cases when the file is
           known by several names in the filesystem.

## [](#BUGS)BUGS

           There are race conditions in the recursive directory watching code
           which can cause events to be missed if they occur in a directory
           immediately after that directory is created.  This is probably not
           fixable.

           It is assumed the inotify event queue will never overflow.

## [](#AUTHORS)AUTHORS

           inotifywatch was started by Rohan McGovern, and is currently
           maintained by Eric Curtin and Radu Voicilas.
           https://www.openhub.net/p/inotify-tools/contributors/summary gives
           you a more complete list of contributors.

           inotifywatch is part of inotify-tools.  The inotify-tools website
           is located at: https://github.com/inotify-tools/inotify-tools/wiki 

## [](#SEE_ALSO)SEE ALSO

           inotifywait(1), inotify(7)

## [](#COLOPHON)COLOPHON

           This page is part of the inotify-tools (command-line programs
           providing a simple interface to inotify) project.  Information
           about the project can be found at 
           ⟨https://github.com/rvoicilas/inotify-tools/wiki⟩.  If you have a
           bug report for this manual page, send it to
           inotify-tools-general@lists.sourceforge.net.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/rvoicilas/inotify-tools.git⟩ on 2026-08-04.
           (At that time, the date of the most recent commit that was found
           in the repository was 2025-09-24.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    inotifywatch 4.23.9.0           2023-09-23                inotifywatch(1)

------------------------------------------------------------------------

Pages that refer to this page: [inotifywait(1)](../man1/inotifywait.1.html),  [inotify(7)](../man7/inotify.7.html)

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
