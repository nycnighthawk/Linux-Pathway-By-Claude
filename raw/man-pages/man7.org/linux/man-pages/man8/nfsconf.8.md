---
{"title": "nfsconf(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/nfsconf.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfsconf(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nfsconf(8)               System Manager's Manual               nfsconf(8)

## [](#NAME)NAME

           nfsconf - Query various NFS configuration settings

## [](#SYNOPSIS)SYNOPSIS

           nfsconf --dump [-v|--verbose] [-f|--file infile.conf] [outfile]

           nfsconf --entry [--arg subsection] section tag

           nfsconf --get [-v|--verbose] [-f|--file infile.conf] [-a|--arg
           subsection] section tag

           nfsconf --isset [-v|--verbose] [-f|--file infile.conf] [-a|--arg
           subsection] section tag

           nfsconf --set [-v|--verbose] [-m|--modified Modified by text]
           [-f|--file infile.conf] [-a|--arg subsection] section tag value

           nfsconf --unset [-v|--verbose] [-f|--file infile.conf] [-a|--arg
           subsection] section tag

## [](#DESCRIPTION)DESCRIPTION

           The nfsconf command can be used to test for and retrieve
           configuration settings from a range of nfs-utils configuration
           files.

       Modes
           The following modes are available:

           -d, --dump
                  Output an alphabetically sorted dump of the current
                  configuration in conf file format. Accepts an optional
                  filename in which to write the output.

           -e, --entry
                  retrieve the config entry rather than its current expanded
                  value

           -i, --isset
                  Test if a specific tag has a value set.

           -g, --get
                  Output the current value of the specified tag.

           -s, --set
                  Update or Add a tag and value to the config file in a
                  specified section, creating the tag, section, and file if
                  necessary. If the section is defined as '#' then a comment
                  is appended to the file. If a comment is set with a tag
                  name then any exiting tagged comment with a matching name
                  is replaced.

           -u, --unset
                  Remove the specified tag and its value from the config
                  file.

## [](#OPTIONS)OPTIONS

       Options valid in all modes
           -v, --verbose
                  Increase verbosity and print debugging information.

           -f, --file infile
                  Select a different config file to operate upon, default is
                  /etc/nfs.conf

       Options only valid in --entry and --get and --isset modes.
           -a, --arg subsection
                  Select a specific sub-section

       Options only valid in --set mode.
           -m, --modified "Modified by nfsconf" Set the text on the Modified
           date comment in the file. Set to empty to remove.

## [](#EXIT_STATUS)EXIT STATUS

       --isset mode
           In this mode the command will return success (0) if the selected
           tag has a value, any other exit code indicates the value is not
           set, or some other error has occurred.

       all other modes
           Success is indicated by an exit status of zero, any other status
           indicates an error. Error messages are output on stderr, and
           increasing verbosity will give more detailed explanations if any
           are available.

## [](#EXAMPLES)EXAMPLES

           nfsconf -v --dump --file /tmp/testconf.conf sorted.conf
                  Check a new config file for syntax errors and output a
                  sorted version for ease of comparison with existing
                  settings.

           if ! nfsconf --isset gssd preferred-realm ; then echo 'No
           preferred realm configured for gss'; fi
                  The tool allows for easy testing of configuration values
                  from shell scripts, here we test if a specific value has
                  been set.

           nfsconf --file /etc/nfsmount.conf --get --arg /home MountPoint
           background
                  Show default value for background option for NFS mounts of
                  the /home path.

           nfsconf --file /etc/nfs.conf --set nfsd debug 1
                  Enable debugging in nfsd

## [](#FILES)FILES

           /etc/nfs.conf

## [](#SEE_ALSO)SEE ALSO

           nfsd(8), exportfs(8), idmapd(8), statd(8)

## [](#AUTHOR)AUTHOR

           Justin Mitchell <jumitche@redhat.com>

## [](#COLOPHON)COLOPHON

           This page is part of the nfs-utils (NFS utilities) project.
           Information about the project can be found at 
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  If you have a bug
           report for this manual page, see
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨git://git.linux-nfs.org/projects/steved/nfs-utils.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-23.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                    2 May 2018                     nfsconf(8)

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
