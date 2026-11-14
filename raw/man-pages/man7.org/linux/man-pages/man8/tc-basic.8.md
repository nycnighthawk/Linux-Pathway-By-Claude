---
{"title": "tc-basic(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/tc-basic.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# tc-basic(8) --- Linux manual page

+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                |                                   |
+------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    Basic classifier in tc(8)         Linux         Basic classifier in tc(8)

## [](#NAME)NAME

           basic - basic traffic control filter

## [](#SYNOPSIS)SYNOPSIS

           tc filter ... basic [ match EMATCH_TREE ] [ action ACTION_SPEC ] [
                   classid CLASSID ]

## [](#DESCRIPTION)DESCRIPTION

           The basic filter allows one to classify packets using the extended
           match infrastructure.

## [](#OPTIONS)OPTIONS

           action ACTION_SPEC
                  Apply an action from the generic actions framework on
                  matching packets.

           classid CLASSID
                  Push matching packets into the class identified by CLASSID.

           match EMATCH_TREE
                  Match packets using the extended match infrastructure. See
                  tc-ematch(8) for a detailed description of the allowed
                  syntax in EMATCH_TREE.

## [](#SEE_ALSO)SEE ALSO

           tc(8), tc-ematch(8)

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

    iproute2                       21 Oct 2015      Basic classifier in tc(8)

------------------------------------------------------------------------

Pages that refer to this page: [tc(8)](../man8/tc.8.html)

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
