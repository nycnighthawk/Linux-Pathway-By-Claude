---
{"title": "systemd-journal-remote.service(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-journal-remote.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-journal-remote.service(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SOURCES](#SOURCES) \| [SINKS](#SINKS) \| [OPTIONS](#OPTIONS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD....SERVICE(8) systemd-journal-remote.serviceSYSTEMD....SERVICE(8)

## [](#NAME)NAME

           systemd-journal-remote.service, systemd-journal-remote.socket,
           systemd-journal-remote - Receive journal messages over the network

## [](#SYNOPSIS)SYNOPSIS

           systemd-journal-remote.service

           systemd-journal-remote.socket

           /usr/lib/systemd/systemd-journal-remote [OPTIONS...]
                                                   [-o/--output=DIR|FILE]
                                                   [SOURCES...]

## [](#DESCRIPTION)DESCRIPTION

           systemd-journal-remote is a command to receive serialized journal
           events and store them to journal files. Input streams are in the
           Journal Export Format[1], i.e. like the output from journalctl
           --output=export. For transport over the network, this serialized
           stream is usually carried over an HTTPS connection.

           systemd-journal-remote.service is a system service that uses
           systemd-journal-remote to listen for connections.
           systemd-journal-remote.socket configures the network address that
           systemd-journal-remote.service listens on. By default, this is
           port 19532. What connections are accepted and how the received
           data is stored can be configured through the
           journal-remote.conf(5) configuration file.

## [](#SOURCES)SOURCES

           Sources can be either "active" (systemd-journal-remote requests
           and pulls the data), or "passive" (systemd-journal-remote waits
           for a connection and then receives events pushed by the other
           side).

           systemd-journal-remote can read more than one event stream at a
           time. They will be interleaved in the output file. In case of
           "active" connections, each "source" is one stream, and in case of
           "passive" connections, each connection can result in a separate
           stream. Sockets can be configured in "accept" mode (i.e. only one
           connection), or "listen" mode (i.e. multiple connections, each
           resulting in a stream).

           When there are no more connections, and no more can be created
           (there are no listening sockets), then systemd-journal-remote will
           exit.

           Active sources can be specified in the following ways:

           [SOURCES]
               When - is given as a positional argument, events will be read
               from standard input. Other positional arguments will be
               treated as filenames to open and read from.

               Added in version 239.

           --url=ADDRESS
               With the --url=ADDRESS option, events will be retrieved using
               HTTP from ADDRESS. This URL should refer to the root of a
               remote systemd-journal-gatewayd(8) instance, e.g.
               http://some.host:19531/ or https://some.host:19531/.

               Added in version 239.

           --getter='PROG [OPTIONS]'
               Program to invoke to retrieve data. The journal event stream
               must be generated on standard output.

               Examples:

                   --getter='curl "-HAccept: application/vnd.fdo.journal" https://some.host:19531/'

                   --getter='wget --header="Accept: application/vnd.fdo.journal" -O- https://some.host:19531/'

               Added in version 239.

           Passive sources can be specified in the following ways:

           --listen-raw=ADDRESS
               ADDRESS must be an address suitable for ListenStream= (cf.
               systemd.socket(5)).  systemd-journal-remote will listen on
               this socket for connections. Each connection is expected to be
               a stream of journal events.

               Added in version 239.

           --listen-http=ADDRESS, --listen-https=ADDRESS
               ADDRESS must be either a negative integer, in which case it
               will be interpreted as the (negated) file descriptor number,
               or an address suitable for ListenStream= (c.f.
               systemd.socket(5)). In the first case, the server listens on
               port 19532 by default, and the matching file descriptor must
               be inherited through $LISTEN_FDS/$LISTEN_PID. In the second
               case, an HTTP or HTTPS server will be spawned on this port,
               respectively for --listen-http= and --listen-https=.
               Currently, only POST requests to /upload with "Content-Type:
               application/vnd.fdo.journal" are supported.

               Added in version 239.

           $LISTEN_FDS
               systemd-journal-remote supports the $LISTEN_FDS/$LISTEN_PID
               protocol. Open sockets inherited through socket activation
               behave like those opened with --listen-raw= described above,
               unless they are specified as an argument in --listen-http=-n
               or --listen-https=-n above. In the latter case, an HTTP or
               HTTPS server will be spawned using this descriptor and
               connections must be made over the HTTP protocol.

               Added in version 239.

           --key=
               Takes a path to a SSL secret key file in PEM format. Defaults
               to /etc/ssl/private/journal-remote.pem. This option can be
               used with --listen-https=. If the path refers to an AF_UNIX
               stream socket in the file system a connection is made to it
               and the key read from it.

               Added in version 239.

           --cert=
               Takes a path to a SSL certificate file in PEM format. Defaults
               to /etc/ssl/certs/journal-remote.pem. This option can be used
               with --listen-https=. If the path refers to an AF_UNIX stream
               socket in the file system a connection is made to it and the
               certificate read from it.

               Added in version 239.

           --trust=
               Takes a path to a SSL CA certificate file in PEM format, or
               all. If all is set, then certificate checking will be
               disabled. Defaults to /etc/ssl/ca/trusted.pem. This option can
               be used with --listen-https=. If the path refers to an AF_UNIX
               stream socket in the file system a connection is made to it
               and the certificate read from it.

               Added in version 239.

           --gnutls-log=
               Takes a comma separated list of gnutls logging categories.
               This option can be used with --listen-http= or
               --listen-https=.

               Added in version 239.

## [](#SINKS)SINKS

           The location of the output journal can be specified with -o or
           --output=.

           -o FILE, --output=FILE
               Will write to this journal file. The filename must end with
               .journal. The file will be created if it does not exist. If
               necessary (journal file full, or corrupted), the file will be
               renamed following normal journald rules and a new journal file
               will be created in its stead.

               Added in version 239.

           -o DIR, --output=DIR
               Will create journal files underneath directory DIR. The
               directory must exist. If necessary (journal files over size,
               or corrupted), journal files will be rotated following normal
               journald rules. Names of files underneath DIR will be
               generated using the rules described below.

               Added in version 239.

           If --output= is not used, the output directory
           /var/log/journal/remote/ will be used. In case the output file is
           not specified, journal files will be created underneath the
           selected directory. Files will be called remote-hostname.journal,
           where the hostname part is the escaped hostname of the source
           endpoint of the connection, or the numerical address if the
           hostname cannot be determined.

           In the case that "active" sources are given by the positional
           arguments or --getter= option, the output file name must always be
           given explicitly.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           --split-mode
               One of none or host. For the first, only one output journal
               file is used. For the latter, a separate output file is used,
               based on the hostname of the other endpoint of a connection.

               In the case that "active" sources are given by the positional
               arguments or --getter= option, the output file name must
               always be given explicitly and only none is allowed.

               Added in version 239.

           --compress [BOOL]
               If this is set to "yes" then compress the data in the journal
               using XZ. The default is "yes".

               Added in version 239.

           --seal [BOOL]
               If this is set to "yes" then periodically sign the data in the
               journal using Forward Secure Sealing. The default is "no".

               Added in version 239.

           --max-use=, --keep-free=, --max-file-size=, --max-files=
               These options override the corresponding settings from the
               configuration file (see journal-remote.conf(5)). See that page
               for the descriptions of these options.

               Added in version 261.

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

## [](#EXAMPLES)EXAMPLES

           Copy local journal events to a different journal directory:

               journalctl -o export | systemd-journal-remote -o /tmp/dir/foo.journal -

           Retrieve all available events from a remote
           systemd-journal-gatewayd(8) instance and store them in
           /var/log/journal/remote/remote-some.host.journal:

               systemd-journal-remote --url http://some.host:19531/

           Retrieve current boot events and wait for new events from a remote
           systemd-journal-gatewayd(8) instance, and store them in
           /var/log/journal/remote/remote-some.host.journal:

               systemd-journal-remote --url http://some.host:19531/entries?boot&follow

## [](#SEE_ALSO)SEE ALSO

           journal-remote.conf(5), journalctl(1),
           systemd-journal-gatewayd.service(8),
           systemd-journal-upload.service(8), systemd-journald.service(8)

## [](#NOTES)NOTES

            1. Journal Export Format
               https://systemd.io/JOURNAL_EXPORT_FORMATS#journal-export-format

## [](#COLOPHON)COLOPHON

           This page is part of the systemd (systemd system and service
           manager) project.  Information about the project can be found at
           ⟨http://www.freedesktop.org/wiki/Software/systemd⟩.  If you have a
           bug report for this manual page, see
           ⟨http://www.freedesktop.org/wiki/Software/systemd/#bugreports⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/systemd/systemd.git⟩ on 2026-08-04.  (At that
           time, the date of the most recent commit that was found in the
           repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    systemd 262~devel                                   SYSTEMD....SERVICE(8)

------------------------------------------------------------------------

Pages that refer to this page: [journalctl(1)](../man1/journalctl.1.html),  [systemd-nspawn(1)](../man1/systemd-nspawn.1.html),  [systemd-vmspawn(1)](../man1/systemd-vmspawn.1.html),  [journald.conf(5)](../man5/journald.conf.5.html),  [journal-remote.conf(5)](../man5/journal-remote.conf.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-journal-gatewayd.service(8)](../man8/systemd-journal-gatewayd.service.8.html),  [systemd-journal-upload.service(8)](../man8/systemd-journal-upload.service.8.html)

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
