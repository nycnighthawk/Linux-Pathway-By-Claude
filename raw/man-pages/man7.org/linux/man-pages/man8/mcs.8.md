---
{"title": "mcs(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/mcs.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# mcs(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [FILES](#FILES) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                   |                                   |
+-------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    mcs(8)                      mcs documentation                      mcs(8)

## [](#NAME)NAME

           mcs - Multi-Category System

## [](#DESCRIPTION)DESCRIPTION

           MCS (Multiple Category System) allows users to label files on
           their system within administrator defined categories.  It then
           uses SELinux Mandatory Access Control to protect those files.
           MCS is a discretionary model to allow users to mark their data
           with additional tags that further restrict access.  The only
           mandatory aspect is authorizing users for categories by defining
           their clearance in policy.  However, MCS is similar to MLS and
           exercises the same code paths and share the same support
           infrastructure.  They just differ in their specific configuration.

           The /etc/selinux/{SELINUXTYPE}/setrans.conf configuration file
           translates the labels on disk to human readable form.
           Administrators can define any labels they want in this file.
           Certain applications like printing and auditing will use these
           labels to identify the files.  By setting a category on a file you
           will prevent other applications/services from having access to the
           files.

           Examples of file labels would be PatientRecord,
           CompanyConfidential etc.

## [](#SEE_ALSO)SEE ALSO

           selinux(8), chcon(1)

## [](#FILES)FILES

           /etc/selinux/{SELINUXTYPE}/setrans.conf

## [](#COLOPHON)COLOPHON

           This page is part of the selinux (Security-Enhanced Linux user-
           space libraries and tools) project.  Information about the project
           can be found at ⟨https://github.com/SELinuxProject/selinux/wiki⟩.
           If you have a bug report for this manual page, see
           ⟨https://github.com/SELinuxProject/selinux/wiki/Contributing⟩.
           This page was obtained from the project's upstream Git repository
           ⟨https://github.com/SELinuxProject/selinux⟩ on 2026-08-04.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-03.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    dwalsh@redhat.com               8 Sep 2005                         mcs(8)

------------------------------------------------------------------------

Pages that refer to this page: [setrans.conf(5)](../man5/setrans.conf.5.html),  [mcstransd(8)](../man8/mcstransd.8.html)

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
