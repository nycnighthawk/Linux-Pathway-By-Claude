---
{"title": "systemd-socket-proxyd(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/systemd-socket-proxyd.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# systemd-socket-proxyd(8) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [EXIT STATUS](#EXIT_STATUS) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                           |                                   |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    SYSTEMD-SOCKET-PROXYD(8)  systemd-socket-proxyd  SYSTEMD-SOCKET-PROXYD(8)

## [](#NAME)NAME

           systemd-socket-proxyd - Bidirectionally proxy local sockets to
           another (possibly remote) socket

## [](#SYNOPSIS)SYNOPSIS

           systemd-socket-proxyd [OPTIONS...] HOST:PORT

           systemd-socket-proxyd [OPTIONS...] UNIX-DOMAIN-SOCKET-PATH

## [](#DESCRIPTION)DESCRIPTION

           systemd-socket-proxyd is a generic socket-activated network socket
           forwarder proxy daemon for IPv4, IPv6 and UNIX stream sockets. It
           may be used to bi-directionally forward traffic from a local
           listening socket to a local or remote destination socket.

           One use of this tool is to provide socket activation support for
           services that do not natively support socket activation. On behalf
           of the service to activate, the proxy inherits the socket from
           systemd, accepts each client connection, opens a connection to a
           configured server for each client, and then bidirectionally
           forwards data between the two.

           This utility's behavior is similar to socat(1). The main
           differences for systemd-socket-proxyd are support for socket
           activation with "Accept=no" and an event-driven design that scales
           better with the number of connections.

           Note that systemd-socket-proxyd will not forward socket side
           channel information, i.e. will not forward SCM_RIGHTS,
           SCM_CREDENTIALS, SCM_SECURITY, SO_PEERCRED, SO_PEERPIDFD,
           SO_PEERSEC, SO_PEERGROUPS and similar.

## [](#OPTIONS)OPTIONS

           The following options are understood:

           -h, --help
               Print a short help text and exit.

           --version
               Print a short version string and exit.

           --connections-max=, -c
               Sets the maximum number of simultaneous connections, defaults
               to 256. If the limit of concurrent connections is reached
               further connections will be refused.

               Added in version 233.

           --exit-idle-time=
               Sets the time before exiting when there are no connections,
               defaults to infinity. Takes a unit-less value in seconds, or a
               time span value such as "5min 20s".

               Added in version 246.

           --proxy-protocol=
               Uses the PROXY protocol[1] to communicate with the server.
               This allows an appropriately configured server to know the
               real client IP address. Takes the version of the PROXY
               protocol[1] used, and only supports "v1" for now. Default is
               not to use a PROXY protocol.

               Added in version 261.

## [](#EXIT_STATUS)EXIT STATUS

           On success, 0 is returned, a non-zero failure code otherwise.

## [](#EXAMPLES)EXAMPLES

       Simple Example
           Use two services with a dependency and no namespace isolation.

           Example 1. proxy-to-nginx.socket

               [Socket]
               ListenStream=80

               [Install]
               WantedBy=sockets.target

           Example 2. proxy-to-nginx.service

               [Unit]
               Requires=nginx.service
               After=nginx.service
               Requires=proxy-to-nginx.socket
               After=proxy-to-nginx.socket

               [Service]
               Type=notify
               ExecStart=/usr/lib/systemd/systemd-socket-proxyd /run/nginx/socket
               PrivateTmp=yes
               PrivateNetwork=yes

           Example 3. nginx.conf

               [...]
               server {
                   listen       unix:/run/nginx/socket;
                   [...]

           Example 4. Enabling the proxy

               # systemctl enable --now proxy-to-nginx.socket
               $ curl http://localhost:80/

           If nginx.service has StopWhenUnneeded= set, then passing
           --exit-idle-time= to systemd-socket-proxyd allows both services to
           stop during idle periods.

       Namespace Example
           Similar as above, but runs the socket proxy and the main service
           in the same private namespace, assuming that nginx.service has
           PrivateTmp= and PrivateNetwork= set, too.

           Example 5. proxy-to-nginx.socket

               [Socket]
               ListenStream=80

               [Install]
               WantedBy=sockets.target

           Example 6. proxy-to-nginx.service

               [Unit]
               Requires=nginx.service
               After=nginx.service
               Requires=proxy-to-nginx.socket
               After=proxy-to-nginx.socket
               JoinsNamespaceOf=nginx.service

               [Service]
               Type=notify
               ExecStart=/usr/lib/systemd/systemd-socket-proxyd 127.0.0.1:8080
               PrivateTmp=yes
               PrivateNetwork=yes

           Example 7. nginx.conf

               [...]
               server {
                   listen       8080;
                   [...]

           Example 8. Enabling the proxy

               # systemctl enable --now proxy-to-nginx.socket
               $ curl http://localhost:80/

       PROXY protocol example with nginx
           systemd-socket-proxyd and nginx using the PROXY protocol

           Example 9. proxy-to-nginx.socket

               [Socket]
               ListenStream=80

               [Install]
               WantedBy=sockets.target

           Example 10. proxy-to-nginx.service

               [Unit]
               Requires=nginx.service
               After=nginx.service
               Requires=proxy-to-nginx.socket
               After=proxy-to-nginx.socket

               [Service]
               Type=notify
               ExecStart=/usr/lib/systemd/systemd-socket-proxyd --proxy-protocol=v1 /run/nginx/socket
               PrivateTmp=yes
               PrivateNetwork=yes

           Example 11. nginx.conf

               [...]
               server {
                   listen         unix:/run/nginx/socket proxy_protocol;
                   real_ip_header proxy_protocol;
                   [...]

           Example 12. Enabling the proxy

               # systemctl enable --now proxy-to-nginx.socket
               $ curl http://localhost:80/

## [](#SEE_ALSO)SEE ALSO

           systemd(1), systemd.socket(5), systemd.service(5), systemctl(1),
           socat(1), nginx(1), curl(1), PROXY protocol specification[1],
           nginx: Accepting the PROXY Protocol[2]

## [](#NOTES)NOTES

            1. PROXY protocol
               https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt

            2. nginx: Accepting the PROXY Protocol
               https://docs.nginx.com/nginx/admin-guide/load-balancer/using-proxy-protocol/

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

    systemd 262~devel                                SYSTEMD-SOCKET-PROXYD(8)

------------------------------------------------------------------------

Pages that refer to this page: [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html)

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
