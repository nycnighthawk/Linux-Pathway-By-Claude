---
{"title": "pam_cap(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/pam_cap.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# pam_cap(8) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    PAM_CAP(8)               System Manager's Manual               PAM_CAP(8)

## [](#NAME)NAME

           pam_cap - Capabilities PAM module

## [](#SYNOPSIS)SYNOPSIS

           [service-name] auth control-flag pam_cap [options]

## [](#DESCRIPTION)DESCRIPTION

           The pam_so module can be used to specify Inheritable capabilities
           to process trees rooted in the PAM application. The module also
           supports blocking Bounding vector capabilities and adding Ambient
           vector capabilities.

           For general PAM apps to work correctly, the application must be
           run with at least CAP_SETPCAP raised in its Permitted capability
           flag. Many PAM applications run as root, which has all of the bits
           in the Bounding set raised, so this requirement is typically met.
           To grant an Ambient vector capability, the corresponding Permitted
           bit must be available to the application too.

           The pam_so module is a Linux-PAM auth module. It provides
           functionality to back pam_sm_authenticate() and pam_sm_setcred().
           It is the latter that actually modifies the inheritable 3-tuple of
           capability vectors: the configured IAB. In a typical application
           configuration you might have a line like this:

               auth    optional    pam_cap.so

           The module arguments are:

           ○   debug: While supported, this is a no-op at present.

           ○   config=/path/to/file: Override the default config for the
               module. The unspecified default value for this file is
               /etc/security/capability.conf. Note, config=/dev/null is a
               valid value. See default= below for situations in which this
               might be appropriate.

           ○   keepcaps: This is as much as the pam_cap.so module can do to
               help an application support use of the Ambient capability
               vector. The application support for the Ambient set is poor at
               the present time.

           ○   autoauth: This argument causes the pam_cap.so module to return
               PAM_SUCCESS if the PAM_USER being authenticated exists. The
               absence of this argument will cause pam_cap.so to only return
               PAM_SUCCESS if the PAM_USER is covered by a specific rule in
               the prevailing config file.

           ○   default=IAB: This argument is ignored if the prevailing
               configuration file contains a "*" rule. If there is no such
               rule, the IAB 3-tuple is inserted at the end of the config
               file and applies to all PAM_USERs not covered by an earlier
               rule. Note, if you want all PAM_USERs to be covered by this
               default rule, you can supply the module argument
               config=/dev/null.

           ○   defer: This argument arranges for the IAB capabilities granted
               to a user to be added sufficiently late in the Linux-PAM
               authentication stack that they stick. That is, after the
               application does its setuid(UID) call. As such, in conjunction
               with the keepcaps module argument, such compliant applications
               can support granting Ambient vector capabilities with
               pam_cap.so.

## [](#SEE_ALSO)SEE ALSO

           pam.conf(5), capability.conf(5), cap_text_formats(7), pam(8).

## [](#COLOPHON)COLOPHON

           This page is part of the libcap (capabilities commands and
           library) project.  Information about the project can be found at
           ⟨https://sites.google.com/site/fullycapable/⟩.  If you have a bug
           report for this manual page, send it to morgan@kernel.org (please
           put "libcap" in the Subject line).  This page was obtained from
           the project's upstream Git repository
           ⟨https://git.kernel.org/pub/scm/libs/libcap/libcap.git/⟩ on
           2026-08-04.  (At that time, the date of the most recent commit
           that was found in the repository was 2026-07-30.)  If you discover
           any rendering problems in this HTML version of the page, or you
           believe there is a better or more up-to-date source for the page,
           or you have corrections or improvements to the information in this
           COLOPHON (which is not part of the original manual page), send a
           mail to man-pages@man7.org

                                    2025-03-19                     PAM_CAP(8)

------------------------------------------------------------------------

Pages that refer to this page: [capability.conf(5)](../man5/capability.conf.5.html),  [cap_text_formats(7)](../man7/cap_text_formats.7.html)

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
