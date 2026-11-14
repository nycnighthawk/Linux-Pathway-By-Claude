---
{"title": "vsock(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/vsock.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# vsock(7) --- Linux manual page

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [ERRORS](#ERRORS) \| [VERSIONS](#VERSIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                       |                                   |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    vsock(7)             Miscellaneous Information Manual            vsock(7)

## [](#NAME)NAME

           vsock - Linux VSOCK address family

## [](#SYNOPSIS)SYNOPSIS

           #include <sys/socket.h>
           #include <linux/vm_sockets.h>

           stream_socket = socket(AF_VSOCK, SOCK_STREAM, 0);
           datagram_socket = socket(AF_VSOCK, SOCK_DGRAM, 0);

## [](#DESCRIPTION)DESCRIPTION

           The VSOCK address family facilitates communication between virtual
           machines and the host they are running on.  This address family is
           used by guest agents and hypervisor services that need a
           communications channel that is independent of virtual machine
           network configuration.

           Valid socket types are SOCK_STREAM and SOCK_DGRAM.  SOCK_STREAM
           provides connection-oriented byte streams with guaranteed, in-
           order delivery.  SOCK_DGRAM provides a connectionless datagram
           packet service with best-effort delivery and best-effort ordering.
           Availability of these socket types is dependent on the underlying
           hypervisor.

           A new socket is created with

               socket(AF_VSOCK, socket_type, 0);

           When a process wants to establish a connection, it calls
           connect(2) with a given destination socket address.  The socket is
           automatically bound to a free port if unbound.

           A process can listen for incoming connections by first binding to
           a socket address using bind(2) and then calling listen(2).

           Data is transmitted using the send(2) or write(2) families of
           system calls and data is received using the recv(2) or read(2)
           families of system calls.

       Address format
           A socket address is defined as a combination of a 32-bit Context
           Identifier (CID) and a 32-bit port number.  The CID identifies the
           source or destination, which is either a virtual machine or the
           host.  The port number differentiates between multiple services
           running on a single machine.

               struct sockaddr_vm {
                   sa_family_t    svm_family;    /* Address family: AF_VSOCK */
                   unsigned short svm_reserved1;
                   unsigned int   svm_port;      /* Port # in host byte order */
                   unsigned int   svm_cid;       /* Address in host byte order */
                   unsigned char  svm_zero[sizeof(struct sockaddr) -
                                           sizeof(sa_family_t) -
                                           sizeof(unsigned short) -
                                           sizeof(unsigned int) -
                                           sizeof(unsigned int)];
               };

           svm_family is always set to AF_VSOCK.  svm_reserved1 is always set
           to 0.  svm_port contains the port number in host byte order.  The
           port numbers below 1024 are called privileged ports.  Only a
           process with the CAP_NET_BIND_SERVICE capability may bind(2) to
           these port numbers.  svm_zero must be zero-filled.

           There are several special addresses: VMADDR_CID_ANY (-1U) means
           any address for binding; VMADDR_CID_HYPERVISOR (0) is reserved for
           services built into the hypervisor; VMADDR_CID_LOCAL (1) is the
           well-known address for local communication (loopback);
           VMADDR_CID_HOST (2) is the well-known address of the host.

           The special constant VMADDR_PORT_ANY (-1U) means any port number
           for binding.

       Live migration
           Sockets are affected by live migration of virtual machines.
           Connected SOCK_STREAM sockets become disconnected when the virtual
           machine migrates to a new host.  Applications must reconnect when
           this happens.

           The local CID may change across live migration if the old CID is
           not available on the new host.  Bound sockets are automatically
           updated to the new CID.

       Ioctls
           The following ioctls are available on the /dev/vsock device.

           IOCTL_VM_SOCKETS_GET_LOCAL_CID
                  Get the CID of the local machine.  The argument is a
                  pointer to an unsigned int.

                      ioctl(fd, IOCTL_VM_SOCKETS_GET_LOCAL_CID, &cid);

                  Consider using VMADDR_CID_ANY when binding instead of
                  getting the local CID with IOCTL_VM_SOCKETS_GET_LOCAL_CID.

       Local communication
           VMADDR_CID_LOCAL (1) directs packets to the same host that
           generated them.  This is useful for testing applications on a
           single host and for debugging.

           The local CID obtained with IOCTL_VM_SOCKETS_GET_LOCAL_CID can be
           used for the same purpose, but it is preferable to use
           VMADDR_CID_LOCAL.

## [](#ERRORS)ERRORS

           EACCES Unable to bind to a privileged port without the
                  CAP_NET_BIND_SERVICE capability.

           EADDRINUSE
                  Unable to bind to a port that is already in use.

           EADDRNOTAVAIL
                  Unable to find a free port for binding or unable to bind to
                  a nonlocal CID.

           EINVAL Invalid parameters.  This includes: attempting to bind a
                  socket that is already bound, providing an invalid struct
                  sockaddr_vm, and other input validation errors.

           ENOPROTOOPT
                  Invalid socket option in setsockopt(2) or getsockopt(2).

           ENOTCONN
                  Unable to perform operation on an unconnected socket.

           EOPNOTSUPP
                  Operation not supported.  This includes: the MSG_OOB flag
                  that is not implemented for the send(2) family of syscalls
                  and MSG_PEEK for the recv(2) family of syscalls.

           EPROTONOSUPPORT
                  Invalid socket protocol number.  The protocol should always
                  be 0.

           ESOCKTNOSUPPORT
                  Unsupported socket type in socket(2).  Only SOCK_STREAM and
                  SOCK_DGRAM are valid.

## [](#VERSIONS)VERSIONS

           Support for VMware (VMCI) has been available since Linux 3.9.  KVM
           (virtio) is supported since Linux 4.8.  Hyper-V is supported since
           Linux 4.14.

           VMADDR_CID_LOCAL is supported since Linux 5.6.  Local
           communication in the guest and on the host is available since
           Linux 5.6.  Previous versions supported only local communication
           within a guest (not on the host), and with only some transports
           (VMCI and virtio).

## [](#SEE_ALSO)SEE ALSO

           bind(2), connect(2), listen(2), recv(2), send(2), socket(2),
           capabilities(7)

## [](#COLOPHON)COLOPHON

           This page is part of the man-pages (Linux kernel and C library
           user-space interface documentation) project.  Information about
           the project can be found at 
           ⟨https://www.kernel.org/doc/man-pages/⟩.  If you have a bug report
           for this manual page, see
           ⟨https://git.kernel.org/pub/scm/docs/man-pages/man-pages.git/tree/CONTRIBUTING⟩.
           This page was obtained from the tarball man-pages-6.19.tar.gz
           fetched from
           ⟨https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/⟩ on
           2026-09-09.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Linux man-pages 6.19            2025-05-17                       vsock(7)

------------------------------------------------------------------------

Pages that refer to this page: [lsfd(1)](../man1/lsfd.1.html),  [systemd-ssh-issue(1)](../man1/systemd-ssh-issue.1.html),  [systemd-ssh-proxy(1)](../man1/systemd-ssh-proxy.1.html),  [trace-cmd-agent(1)](../man1/trace-cmd-agent.1.html),  [socket(2)](../man2/socket.2.html),  [org.freedesktop.hostname1(5)](../man5/org.freedesktop.hostname1.5.html),  [address_families(7)](../man7/address_families.7.html),  [systemd-ssh-generator(8)](../man8/systemd-ssh-generator.8.html)

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
