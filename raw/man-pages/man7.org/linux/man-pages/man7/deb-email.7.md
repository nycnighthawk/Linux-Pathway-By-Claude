---
{"title": "deb-email(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/deb-email.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# deb-email(7) --- Linux manual page

+------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [COLOPHON](#COLOPHON) |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                |                                   |
+------------------------------------------------------------------------------------------------+-----------------------------------+

    deb-email(7)                    dpkg suite                   deb-email(7)

## [](#NAME)NAME

           deb-email - Debian package email address format

## [](#SYNOPSIS)SYNOPSIS

           Näme "quoted, text" S. Surname <näme@exâmple.org>

## [](#DESCRIPTION)DESCRIPTION

           Email addresses as used for Debian package metadata in binary and
           source packages.  These consist of a name, followed by at least
           one space, and then an email address.

           The name is composed of one or more quoted (") or non-quoted
           parts.  These parts can contain any UTF-8 character except for
           angle brackets (<>), double quotes ("), and control characters.  A
           comma (,) is only allowed inside double quoted parts.

           The email address is contained inside angle brackets (<>), and is
           composed of a local part separated by an at sign (@) followed by
           the domain part.

           Both local and domain parts can contain any UTF-8 character except
           for angle brackets (<>), at sign (@) double quotes ("), space ( ),
           and control characters.

           Note: A domain part with a single label is allowed but will emit a
           warning, as those domains are either for local hosts, or a TLD
           which are not supposed to receive mail.

           Note: A domain part is expected to be encoded in UTF-8, and not in
           IDNA/Punycode, for readability and general handling reasons.

           Multiple addresses must be separated with a comma.

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

    1.23.7-216-gff7e9               2026-03-07                   deb-email(7)

------------------------------------------------------------------------

Pages that refer to this page: [dpkg-genchanges(1)](../man1/dpkg-genchanges.1.html),  [dpkg-parsechangelog(1)](../man1/dpkg-parsechangelog.1.html),  [deb-changelog(5)](../man5/deb-changelog.5.html),  [deb-changes(5)](../man5/deb-changes.5.html),  [deb-control(5)](../man5/deb-control.5.html),  [deb-src-control(5)](../man5/deb-src-control.5.html),  [dsc(5)](../man5/dsc.5.html)

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
