---
{"title": "deb-triggers(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/deb-triggers.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-triggers(5) --- Linux manual page

+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                         |                                   |
+-------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-triggers(5)                 dpkg suite                deb-triggers(5)

## [](#NAME)NAME

           deb-triggers - package triggers

## [](#SYNOPSIS)SYNOPSIS

           debian/triggers, debian/binary-package.triggers, DEBIAN/triggers

## [](#DESCRIPTION)DESCRIPTION

           A package declares its relationship to some trigger(s) by
           including a triggers file in its control archive (i.e.
           DEBIAN/triggers during package creation).

           This file contains directives, one per line.  Leading and trailing
           whitespace and everything after the first # on any line will be
           trimmed, and empty lines will be ignored.

           The trigger control directives currently supported are:

           interest trigger-name
           interest-await trigger-name
           interest-noawait trigger-name
               Specifies that the package is interested in the named trigger.
               All triggers in which a package is interested must be listed
               using this directive in the triggers control file.

               The “await” variants put the triggering package in
               triggers-awaited state depending on how the trigger was
               activated.  The “noawait” variant does not put the triggering
               packages in triggers-awaited state, even if the triggering
               package declared an “await” activation (either with an
               activate-await or activate directive, or by using the
               dpkg-trigger --no-await command-line option).  The “noawait”
               variant should be used when the functionality provided by the
               trigger is not crucial.

           activate trigger-name
           activate-await trigger-name
           activate-noawait trigger-name
               Arranges that changes to this package's state will activate
               the specified trigger.  The trigger will be activated at the
               start of the following operations: unpack, configure, remove
               (including for the benefit of a conflicting package), purge
               and deconfigure.

               The “await” variants only put the triggering package in
               triggers-awaited state if the interest directive is also
               “await”.  The “noawait” variant never puts the triggering
               packages in triggers-awaited state.  The “noawait” variant
               should be used when the functionality provided by the trigger
               is not crucial.

               If this package disappears during the unpacking of another
               package the trigger will be activated when the disappearance
               is noted towards the end of the unpack.  Trigger processing,
               and transition from triggers-awaited to installed, does not
               cause activations.  In the case of unpack, triggers mentioned
               in both the old and new versions of the package will be
               activated.

           Unknown directives are an error which will prevent installation of
           the package.

           The “-noawait” variants should always be favored when possible
           since triggering packages are not put in triggers-awaited state
           and can thus be immediately configured without requiring the
           processing of the trigger.  If the triggering packages are
           dependencies of other upgraded packages, it will avoid an early
           trigger processing run and make it possible to run the trigger
           only once as one of the last steps of the upgrade.

           Support for the “-noawait” variants since dpkg 1.16.1, will lead
           to errors if used with an older dpkg.

           Support for the “-await” alias variants since dpkg 1.17.21, will
           lead to errors if used with an older dpkg.

           When a package provides an interest-noawait directive, any
           activation will set the triggering package into “noawait” mode,
           regardless of the awaiting mode requested by the activation
           (either “await” or “noawait”).  When a package provides an
           interest or interest-await directive, any activation will set the
           triggering package into “await” or “noawait“ depending on how it
           was activated.

## [](#SEE_ALSO)SEE ALSO

           dpkg-trigger(1), dpkg(1),
           /usr/local/share/doc/dpkg/spec/triggers.txt.

## [](#COLOPHON)COLOPHON

           This page is part of the dpkg (Debian Package Manager) project.
           Information about the project can be found at 
           ⟨https://wiki.debian.org/Teams/Dpkg/⟩.  If you have a bug report
           for this manual page, see
           ⟨http://bugs.debian.org/cgi-bin/pkgreport.cgi?src=dpkg⟩.  This
           page was obtained from the project's upstream Git repository ⟨git
           clone https://git.dpkg.org/git/dpkg/dpkg.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2026-08-01.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    1.23.7-216-gff7e9               2026-03-07                deb-triggers(5)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-trigger(1)](../man1/dpkg-trigger.1.html),  [deb(5)](../man5/deb.5.html)

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
