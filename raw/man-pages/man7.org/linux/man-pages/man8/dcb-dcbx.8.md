---
{"title": "dcb-dcbx(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/dcb-dcbx.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# dcb-dcbx(8) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [PARAMETERS](#PARAMETERS) \| [EXAMPLE & USAGE](#EXAMPLE_&_USAGE) \| [EXIT STATUS](#EXIT_STATUS) \| [SEE ALSO](#SEE_ALSO) \| [REPORTING BUGS](#REPORTING_BUGS) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                      |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    DCB-DCBX(8)                       Linux                       DCB-DCBX(8)

## [](#NAME)NAME

           dcb-dcbx - show / manipulate port DCBX (Data Center Bridging
           eXchange)

## [](#SYNOPSIS)SYNOPSIS

           dcb [ OPTIONS ] dcbx { COMMAND | help }

           dcb dcbx show dev DEV

           dcb dcbx set dev DEV [ host ] [ lld-managed ] [ cee ] [ ieee ] [
                   static ]

## [](#DESCRIPTION)DESCRIPTION

           Data Center Bridging eXchange (DCBX) is a protocol used by DCB
           devices to exchange configuration information with directly
           connected peers. The Linux DCBX object is a 1-byte bitfield of
           flags that configure whether DCBX is implemented in the device or
           in the host, and which version of the protocol should be used.
           dcb dcbx is used to access the per-port Linux DCBX object.

           There are two principal modes of operation: in host mode, DCBX
           protocol is implemented by the host LLDP agent, and the DCB
           interfaces are used to propagate the negotiate parameters to
           capable devices. In lld-managed mode, the configuration is handled
           by the device, and DCB interfaces are used for inspection of
           negotiated parameters, and can also be used to set initial
           parameters.

## [](#PARAMETERS)PARAMETERS

           When used with dcb dcbx set, the following keywords enable the
           corresponding configuration. The keywords that are not mentioned
           on the command line are considered disabled. When used with show,
           each enabled feature is shown by its corresponding keyword.

           host
           lld-managed
                  The device is in the host mode of operation and,
                  respectively, the lld-managed mode of operation, as
                  described above. In principle these two keywords are
                  mutually exclusive, but dcb dcbx allows setting both and
                  lets the driver handle it as appropriate.

           cee
           ieee   The device supports CEE (Converged Enhanced Ethernet) and,
                  respectively, IEEE version of the DCB specification.
                  Typically only one of these will be set, but dcb dcbx does
                  not mandate this.

           static Indicates the engine supports static configuration. No
                  actual negotiation is performed, negotiated parameters are
                  always the initial configuration.

## [](#EXAMPLE_&_USAGE)EXAMPLE & USAGE

           Put the DCB engine into the "host" mode of operation, and use
           IEEE-standardized DCB interfaces:

           # dcb dcbx set dev eth0 host ieee

           Show what was set:

           # dcb dcbx show dev eth0
           host ieee

## [](#EXIT_STATUS)EXIT STATUS

           Exit status is 0 if command was successful or a positive integer
           upon failure.

## [](#SEE_ALSO)SEE ALSO

           dcb(8)

## [](#REPORTING_BUGS)REPORTING BUGS

           Report any bugs to the Network Developers mailing list
           <netdev@vger.kernel.org> where the development and maintenance is
           primarily done.  You do not have to be subscribed to the list to
           send a message there.

## [](#AUTHOR)AUTHOR

           Petr Machata <me@pmachata.org>

## [](#COLOPHON)COLOPHON

           This page is part of the iproute2 (utilities for controlling
           TCP/IP networking and traffic) project.  Information about the
           project can be found at 
           ⟨http://www.linuxfoundation.org/collaborate/workgroups/networking/iproute2⟩.
           If you have a bug report for this manual page, send it to
           netdev@vger.kernel.org, shemminger@osdl.org.  This page was
           obtained from the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/network/iproute2/iproute2.git⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-28.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

    iproute2                     13 December 2020                 DCB-DCBX(8)

------------------------------------------------------------------------

Pages that refer to this page: [dcb(8)](../man8/dcb.8.html)

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
