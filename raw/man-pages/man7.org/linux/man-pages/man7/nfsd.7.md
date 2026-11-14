---
{"title": "nfsd(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/nfsd.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# nfsd(7) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNPOSIS](#SYNPOSIS) \| [DESCRIPTION](#DESCRIPTION) \| [DETAILS](#DETAILS) \| [NOTES](#NOTES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    nfsd(7)              Miscellaneous Information Manual             nfsd(7)

## [](#NAME)NAME

           nfsd - special filesystem for controlling Linux NFS server

## [](#SYNPOSIS)SYNPOSIS

           mount -t nfsd nfsd /proc/fs/nfsd

## [](#DESCRIPTION)DESCRIPTION

           The nfsd filesystem is a special filesystem which provides access
           to the Linux NFS server.  Writing to files in this filesystem can
           affect the server.  Reading from them can provide information
           about the server.

           As well as this filesystem, there are a collection of files in the
           procfs filesystem (normally mounted at /proc) which are used to
           control the NFS server.  This manual page describes all of these
           files.

           The exportfs and mountd programs (part of the nfs-utils package)
           expect to find this filesystem mounted at /proc/fs/nfsd or
           /proc/fs/nfs.

## [](#DETAILS)DETAILS

           Files in the nfsd filesystem include:

           exports
                  This file contains a list of filesystems that are currently
                  exported and clients that each filesystem is exported to,
                  together with a list of export options for that
                  client/filesystem pair.  This is similar to the
                  /proc/fs/nfs/exports file in 2.4.  One difference is that a
                  client doesn't necessarily correspond to just one host.  It
                  can respond to a large collection of hosts that are being
                  treated identically.

                  Each line of the file contains a path name, a client name,
                  and a number of options in parentheses.  Any space, tab,
                  newline or back-slash character in the path name or client
                  name will be replaced by a backslash followed by the octal
                  ASCII code for that character.

           threads
                  This file represents the number of nfsd thread currently
                  running.  Reading it will show the number of threads.
                  Writing an ASCII decimal number will cause the number of
                  threads to be changed (increased or decreased as necessary)
                  to achieve that number.

           filehandle
                  This is a somewhat unusual file  in that what is read from
                  it depends on what was just written to it.  It provides a
                  transactional interface where a program can open the file,
                  write a request, and read a response.  If two separate
                  programs open, write, and read at the same time, their
                  requests will not be mixed up.

                  The request written to filehandle should be a client name,
                  a path name, and a number of bytes.  This should be
                  followed by a newline, with white-space separating the
                  fields, and octal quoting of special characters.

                  On writing this, the program will be able to read back a
                  filehandle for that path as exported to the given client.
                  The filehandle's length will be at most the number of bytes
                  given.

                  The filehandle will be represented in hex with a leading
                  '\x'.

           clients/
                  This directory contains a subdirectory for each NFSv4
                  client.  Each file under that subdirectory gives some
                  details about the client in YAML format.  In addition,
                  writing "expire\n" to the ctl file will force the server to
                  immediately revoke all state held by that client.

           The directory /proc/net/rpc in the procfs filesystem contains a
           number of files and directories.  The files contain statistics
           that can be display using the nfsstat program.  The directories
           contain information about various caches that the NFS server
           maintains to keep track of access permissions that different
           clients have for different filesystems.  The caches are:

           auth.unix.ip
                  This cache contains a mapping from IP address to the name
                  of the authentication domain that the ipaddress should be
                  treated as part of.

           nfsd.export
                  This cache contains a mapping from directory and domain to
                  export options.

           nfsd.fh
                  This cache contains a mapping from domain and a filesystem
                  identifier to a directory.   The filesystem identifier is
                  stored in the filehandles and consists of a number
                  indicating the type of identifier and a number of hex bytes
                  indicating the content of the identifier.

           Each directory representing a cache can hold from 1 to 3 files.
           They are:

           flush  When a number of seconds since epoch (1 Jan 1970) is
                  written to this file, all entries in the cache that were
                  last updated before that file become invalidated and will
                  be flushed out.  Writing a time in the future (in seconds
                  since epoch) will flush everything.  This is the only file
                  that will always be present.

           content
                  This file, if present, contains a textual representation of
                  ever entry in the cache, one per line.  If an entry is
                  still in the cache (because it is actively being used) but
                  has expired or is otherwise invalid, it will be presented
                  as a comment (with a leading hash character).

           channel
                  This file, if present, acts a channel for request from the
                  kernel-based nfs server to be passed to a user-space
                  program for handling.

                  When the kernel needs some information which isn't in the
                  cache, it makes a line appear in the channel file giving
                  the key for the information.  A user-space program should
                  read this, find the answer, and write a line containing the
                  key, an expiry time, and the content.  For example the
                  kernel might make
                       nfsd 127.0.0.1
                  appear in the auth.unix.ip/content file.  The user-space
                  program might then write
                       nfsd 127.0.0.1 1057206953 localhost
                  to indicate that 127.0.0.1 should map to localhost, at
                  least for now.

                  If the program uses select(2) or poll(2) to discover if it
                  can read from the channel then it will never see and end-
                  of-file but when all requests have been answered, it will
                  block until another request appears.

           In the /proc filesystem there are 4 files that can be used to
           enabled extra tracing of nfsd and related code.  They are:
                /proc/sys/sunrpc/nfs_debug
                /proc/sys/sunrpc/nfsd_debug
                /proc/sys/sunrpc/nlm_debug
                /proc/sys/sunrpc/rpc_debug
           They control tracing for the NFS client, the NFS server, the
           Network Lock Manager (lockd) and the underlying RPC layer
           respectively.  Decimal numbers can be read from or written to
           these files.  Each number represents a bit-pattern where bits that
           are set cause certain classes of tracing to be enabled.  Consult
           the kernel header files to find out what number correspond to what
           tracing.

## [](#NOTES)NOTES

           This file system is only available in Linux 2.6 and later series
           kernels (and in the later parts of the 2.5 development series
           leading up to 2.6).  This man page does not apply to 2.4 and
           earlier.

           Previously the nfsctl systemcall was used for communication
           between nfsd and user utilities.  That systemcall was removed in
           kernel version 3.1.  Older nfs-utils versions were able to fall
           back to nfsctl if necessary; that was removed from nfs-utils
           1.3.5.

## [](#SEE_ALSO)SEE ALSO

           nfsd(8), rpc.nfsd(8), exports(5), nfsstat(8), mountd(8)
           exportfs(8).

## [](#AUTHOR)AUTHOR

           NeilBrown

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

                                   3 July 2003                        nfsd(7)

------------------------------------------------------------------------

Pages that refer to this page: [nfsservctl(2)](../man2/nfsservctl.2.html),  [nfsd(8)](../man8/nfsd.8.html)

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
