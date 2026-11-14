---
{"title": "lxc-user-nic(1) — Linux manual page", "url": "https://man7.org/linux/man-pages/man1/lxc-user-nic.1.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# lxc-user-nic(1) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    lxc-user-nic(1)                                           lxc-user-nic(1)

## [](#NAME)NAME

           lxc-user-nic - Manage nics in another network namespace

## [](#SYNOPSIS)SYNOPSIS

           lxc-user-nic create {lxcpath} {name} {pid} {type} {bridge}
                        {container nicname}
           lxc-user-nic delete {lxcpath} {name} {path to network namespace}
                        {type} {bridge} {container nicname}

## [](#DESCRIPTION)DESCRIPTION

           lxc-user-nic  is  a  setuid-root  program  with which unprivileged
           users may manage network interfaces for use by a lxc container.

           It will consult the configuration file /etc/lxc/lxc-usernet to de‐
           termine the number of interfaces which the calling user is allowed
           to create, and which bridge they may attach them to. It tracks the
           number  of  interfaces  each  user  has  created  using  the  file
           /run/lxc/nics. It ensures that the calling user is privileged over
           the  network  namespace  to  which the interface will be attached.
           lxc-user-nic also allows one to delete network devices.  Currently
           only ovs ports can be deleted.

## [](#OPTIONS)OPTIONS

           lxcpath
                  The path of the container. This is currently not used.

           name   The name of the container. This is currently not used.

           pid    The process id for the task to whose network namespace the
                  interface should be attached.

           type   The network interface type to attach. Currently only veth
                  is supported. With this type, two interfaces representing
                  each tunnel endpoint are created. One endpoint will be at‐
                  tached to the specified bridge, while the other will be
                  passed into the container.

           bridge The bridge to which to attach the network interface, for
                  instance lxcbr0.

           container nicname
                  The desired interface name in the container. This will be
                  eth0 if unspecified.

           path to network namespace
                  A path to open to get a file descriptor for the target net‐
                  work namespace.  This is only relevant when an veth device
                  is deleted.

## [](#SEE_ALSO)SEE ALSO

           lxc(1), lxc-start(1), lxc-usernet(5)

## [](#COLOPHON)COLOPHON

           This page is part of the lxc (Linux containers) project.  Informa‐
           tion about the project can be found at 
           ⟨http://linuxcontainers.org/⟩.  If you have a bug report for this
           manual page, send it to lxc-devel@lists.linuxcontainers.org.  This
           page was obtained from the project's upstream Git repository
           ⟨https://github.com/lxc/lxc.git⟩ on 2026-08-04.  (At that time,
           the date of the most recent commit that was found in the
           repository was 2026-07-23.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

                                    2026-04-29                lxc-user-nic(1)

------------------------------------------------------------------------

Pages that refer to this page: [lxc-usernet(5)](../man5/lxc-usernet.5.html)

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
