---
{"title": "libdrop_ambient(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/libdrop_ambient.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# libdrop_ambient(7) --- Linux manual page

+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [AUTHOR](#AUTHOR) \| [COLOPHON](#COLOPHON) |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                     |                                   |
+---------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    LIBDROP_AMBIENT(7)            Libcap-ng API            LIBDROP_AMBIENT(7)

## [](#NAME)NAME

           libdrop_ambient - force application started with ambient
           capabilities to drop them

## [](#DESCRIPTION)DESCRIPTION

           This library can be used via LD_PRELOAD to force an application
           started with ambient capabilities to drop them. It leaves other
           capabilities intact. This can also be linked against and
           automatically does the right thing. You do not need to make any
           calls into the library because all the work is done in the
           constructor which runs before main() is called.

## [](#SEE_ALSO)SEE ALSO

           capabilities(7)

## [](#AUTHOR)AUTHOR

           Steve Grubb

## [](#COLOPHON)COLOPHON

           This page is part of the libcap-ng (capabilities commands and
           library (NG)) project.  Information about the project can be found
           at ⟨https://people.redhat.com/sgrubb/libcap-ng/⟩.  It is not known
           how to report bugs for this man page; if you know, please send a
           mail to man-pages@man7.org.  This page was obtained from the
           tarball fetched from
           ⟨https://people.redhat.com/sgrubb/libcap-ng/index.html⟩ on
           2026-08-04.  If you discover any rendering problems in this HTML
           version of the page, or you believe there is a better or more up-
           to-date source for the page, or you have corrections or
           improvements to the information in this COLOPHON (which is not
           part of the original manual page), send a mail to
           man-pages@man7.org

    Red Hat                         March 2026             LIBDROP_AMBIENT(7)

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
