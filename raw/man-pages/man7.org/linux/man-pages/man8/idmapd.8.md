---
{"title": "idmapd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/idmapd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# idmapd(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [CONFIGURATION FILES](#CONFIGURATION_FILES) \| [EXAMPLES](#EXAMPLES) \| [FILES](#FILES) \| [SEE ALSO](#SEE_ALSO) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                           |                                   |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    RPC.IDMAPD(8)             System Manager's Manual           RPC.IDMAPD(8)

## [](#NAME)NAME

           rpc.idmapd — NFSv4 ID <-> Name Mapper

## [](#SYNOPSIS)SYNOPSIS

           rpc.idmapd [-h] [-f] [-v] [-C] [-S] [-p path] [-c path]

## [](#DESCRIPTION)DESCRIPTION

           rpc.idmapd is the NFSv4 ID <-> name mapping daemon.  It provides
           functionality to the NFSv4 kernel client and server, to which it
           communicates via upcalls, by translating user and group IDs to
           names, and vice versa.

           The system derives the user part of the string by performing a
           password or group lookup.  The lookup mechanism is configured in
           /etc/idmapd.conf

           By default, the domain part of the string is the system's DNS
           domain name.  It can also be specified in /etc/idmapd.conf if the
           system is multi-homed, or if the system's DNS domain name does not
           match the name of the system's Kerberos realm.

           When the domain is not specified in /etc/idmapd.conf the local DNS
           server will be queried for the _nfsv4idmapdomain text record. If
           the record exists that will be used as the domain. When the record
           does not exist, the domain part of the DNS domain will used.

           Note that on more recent kernels only the NFSv4 server uses
           rpc.idmapd.  The NFSv4 client instead uses nfsidmap(8), and only
           falls back to rpc.idmapd if there was a problem running the
           nfsidmap(8) program.

           The options are as follows:

           -h           Display usage message.

           -v           Increases the verbosity level (can be specified
                        multiple times).

           -f           Runs rpc.idmapd in the foreground and prints all
                        output to the terminal.

           -p path      Specifies the location of the RPC pipefs to be path.
                        The default value is "/var/lib/nfs/rpc_pipefs".

           -c path      Use configuration file path.  This option is
                        deprecated.

           -C           Client-only: perform no idmapping for any NFS server,
                        even if one is detected.

           -S           Server-only: perform no idmapping for any NFS client,
                        even if one is detected.

## [](#CONFIGURATION_FILES)CONFIGURATION FILES

           rpc.idmapd recognizes the following value from the [general]
           section of the /etc/nfs.conf configuration file:

           pipefs-directory
                        Equivalent to -p.

           All other settings related to id mapping are found in the
           /etc/idmapd.conf configuration file.

## [](#EXAMPLES)EXAMPLES

           rpc.idmapd -f -vvv

           Runs rpc.idmapd printing all messages to console, and with a
           verbosity level of 3.

## [](#FILES)FILES

           /etc/idmapd.conf, /etc/nfs.conf

## [](#SEE_ALSO)SEE ALSO

           idmapd.conf(5), nfs.conf(5), nfsidmap(8)

## [](#AUTHORS)AUTHORS

           The rpc.idmapd software has been developed by Marius Aamodt
           Eriksen ⟨marius@citi.umich.edu⟩.

## [](#COLOPHON)COLOPHON

           This page is part of the nfs-utils (NFS utilities) project.
           Information about the project can be found at
           http://linux-nfs.org/wiki/index.php/Main_Page.  If you have a bug
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

    GNU                          February 3, 2003               RPC.IDMAPD(8)

------------------------------------------------------------------------

Pages that refer to this page: [nfs(5)](../man5/nfs.5.html),  [nfs.conf(5)](../man5/nfs.conf.5.html),  [nfsconf(8)](../man8/nfsconf.8.html),  [nfsdclnts(8)](../man8/nfsdclnts.8.html)

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
