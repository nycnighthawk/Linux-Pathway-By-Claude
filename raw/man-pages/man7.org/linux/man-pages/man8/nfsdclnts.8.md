---
{"title": "nfsdclnts(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/nfsdclnts.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfsdclnts(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [NOTES](#NOTES) \| [BUGS](#BUGS) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                       |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    NFSDCLTS(8)                     nfsdclnts                     NFSDCLTS(8)

## [](#NAME)NAME

           nfsdclnts - print various nfs client information for knfsd server.

## [](#SYNOPSIS)SYNOPSIS

           nfsdclnts [-h] [-t type] [--clientinfo] [--hostname] [-q]

## [](#DESCRIPTION)DESCRIPTION

           The nfsdclnts(8) command parses the content present in
           /proc/fs/nfsd/clients/ directories. nfsdclnts(8) displays files
           which are open, locked, delegated by the nfs-client. It also
           prints useful client information such as hostname, clientID, NFS
           version mounted by the nfs-client.

## [](#OPTIONS)OPTIONS

           -t, --type=TYPE
               Specify the type of file to be displayed. Takes only one TYPE
               at a time.

               open, lock, deleg, layout, or all

               open: displays the open files by nfs-client(s).

               lock: displays the files locked by nfs-client(s).

               layout: displays the files for which layout is given.

               deleg: displays delegated files information and delegation
               type.

               all: prints all the above type.

           --clientinfo
               displays various nfs-client info fields such as version of nfs
               mounted at nfs-client and clientID.

           --hostname
               Print hostname of nfs-client instead of ip-address.

           -q, --quiet
               Hide the header information.

           -v, --verbose
               Verbose operation, show debug messages.

           -f, --file
               Instead of processing all client directories under
               /proc/fs/nfsd/clients, one can provide a specific states file
               to process. One should make sure that info file resides in the
               same directory as states file. If the info file is not valid
               or present the fields would be marked as "N/A".

           -h, --help
               Print help explaining the command line options.

## [](#EXAMPLES)EXAMPLES

           nfsdclnts --type open
               List all files with open type only.

               Inode number | Type   | Access | Deny | ip address            | Filename
               33823232     | open   | r-     | --   | [::1]:757             | testfile

           nfsdclnts --type deleg
               List all files with deleg type only.

               Inode number | Type   | Access | ip address            | Filename
               33823232     | deleg  | r      | [::1]:757             | testfile

           nfsdclnts --hostname
               Print hostname instead of ip-address.

               Inode number | Type   | Access | Deny | Hostname              | Filename
               33823232     | open   | r-     | --   | nfs-server            | testfile
               33823232     | deleg  | r      |      | nfs-server            | testfile

           nfsdclnts --clientinfo
               Print client information.

               Inode number | Type   | Access | Deny | ip address            | Client ID           | vers | Filename
               33823232     | open   | r-     | --   | [::1]:757             | 0xc79a009f5eb65e84  | 4.2  | testfile
               33823232     | deleg  | r      |      | [::1]:757             | 0xc79a009f5eb65e84  | 4.2  | testfile

           nfsdclnts --file /proc/fs/nfsd/clients/3/states -t open
               Process specific states file.

               Inode number | Type   | Access | Deny | ip address            | Client ID           | vers | Filename
               33823232     | open   | r-     | --   | [::1]:757             | 0xc79a009f5eb65e84  | 4.2  | testfile

           nfsdclnts --quiet --hostname
               Hide the header information.

               33823232     | open   | r-     | --   | nfs-server            | testfile
               33823232     | deleg  | r      |      | nfs-server            | testfile

## [](#FILES)FILES

           /proc/fs/nfsd/clients/

           Displays basic information about each NFSv4 client.

           /proc/fs/nfsd/clients/#/info

           Displays information about all the opens held by the given client,
           including open modes, device numbers, inode numbers, and open
           owners.

           /proc/fs/nfsd/clients/#/states

## [](#NOTES)NOTES

           /proc/fs/nfsd/clients/ support was initially introduced in 5.3
           kernel and is only implemented for mount points using NFSv4.

## [](#BUGS)BUGS

           Please report any BUGs to linux-nfs@vger.kernel.org

## [](#SEE_ALSO)SEE ALSO

           nfsd(8), exportfs(8), idmapd(8), statd(8)

## [](#AUTHORS)AUTHORS

           Achilles Gaikwad <agaikwad@redhat.com> and Kenneth D'souza
           <kdsouza@redhat.com>

## [](#COLOPHON)COLOPHON

           This page is part of the nfs-utils (NFS utilities) project.
           Information about the project can be found at 
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩. If you have a bug
           report for this manual page, see
           ⟨http://linux-nfs.org/wiki/index.php/Main_Page⟩. This page was
           obtained from the project's upstream Git repository
           ⟨git://git.linux-nfs.org/projects/steved/nfs-utils.git⟩ on
           2026-08-04. (At that time, the date of the most recent commit that
           was found in the repository was 2026-07-23.) If you discover any
           rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    nfsdclnts                       2020-05-09                    NFSDCLTS(8)

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
