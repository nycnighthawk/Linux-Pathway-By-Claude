---
{"title": "hostname(5) — Linux manual page", "url": "https://man7.org/linux/man-pages/man5/hostname.5.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# hostname(5) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [HOSTNAME SEMANTICS](#HOSTNAME_SEMANTICS) \| [HISTORY](#HISTORY) \| [SEE ALSO](#SEE_ALSO) \| [NOTES](#NOTES) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HOSTNAME(5)                      hostname                     HOSTNAME(5)

## [](#NAME)NAME

           hostname - Local hostname configuration file

## [](#SYNOPSIS)SYNOPSIS

           /etc/hostname

## [](#DESCRIPTION)DESCRIPTION

           The /etc/hostname file configures the name of the local system.
           Unless overridden as described in the next section, systemd(1)
           will set this hostname during boot using the sethostname(2) system
           call.

           The file should contain a single newline-terminated hostname
           string. Comments (lines starting with a "#") are ignored. The
           hostname should be composed of up to 64 7-bit ASCII lower-case
           alphanumeric characters or hyphens forming a valid DNS domain
           name. It is strongly recommended that this name contains only a
           single DNS label, i.e does not contain any dots. This
           recommendation reflects both usual expectations of applications,
           and the fact that the Linux kernel limits the length of the system
           hostname to 64 (i.e. close to the maximum DNS label length of 63)
           rather than 255 (the maximum DNS domain name length). When
           applied, invalid characters will be filtered out in an attempt to
           make the name valid, but obviously it is recommended to use a
           valid name and not rely on this filtering.

           If the question mark character "?"  appears in the hostname, it is
           automatically substituted by a hexadecimal character derived from
           the machine-id(5) when applied, securely and deterministically by
           cryptographic hashing. Example: "foobar-????-????"  will
           automatically expand to "foobar-92a9-061c" or similar, depending
           on the local machine ID.

           In addition, the token "$" is substituted by a word picked
           deterministically from a word list, again derived from the
           machine-id(5) by cryptographic hashing. Each "$" is positional:
           the first "$" uses the word list file named 1, the second 2, and
           so on. This allows human-friendly names, for example "$-$-$-????"
           might expand to "wildly-happy-octopus-92a9". The word lists are
           searched for in /etc/systemd/hostname-wordlist/,
           /run/systemd/hostname-wordlist/,
           /usr/local/lib/systemd/hostname-wordlist/ and
           /usr/lib/systemd/hostname-wordlist/ (the first directory providing
           a given list wins, lists are not merged); one word per line, with
           empty lines and lines starting with "#" ignored.

           The word for each token is derived deterministically from the
           machine ID and recomputed on every boot (the lists are not loaded
           wholesale: a word is chosen by hashing to a byte offset into the
           file). Consequently the word lists must be kept stable: changing a
           list (adding, removing, or reordering words) may change the name a
           machine already has, so installations that rely on persistent
           hostnames must not modify the lists after deployment. If a
           referenced list is missing the name is treated as invalid and the
           built-in fallback hostname is used. The combined name space is the
           product of the list sizes, so collisions follow the birthday
           bound; append a few "?"  characters for extra entropy when
           uniqueness across a large fleet matters.

           Note that hostname can be at most 64 characters long. The word
           lists and the pattern should be chosen so that the longest
           possible expansion (the longest words from each list plus any
           literal and "?"  characters and separators) stays within this
           limit. An expanded name that exceeds the limit is considered
           invalid and the built-in fallback hostname is used.

           Because the name only stays stable as long as the pattern and word
           lists are unchanged, the preferred way to obtain a stable,
           generated hostname is to provide the pattern through the
           firstboot.hostname credential (see systemd.system-credentials(7))
           rather than placing it directly in this file. Concretely, write
           the pattern to /etc/credstore/firstboot.hostname (see the
           description of LoadCredential= in systemd.exec(5) for the
           credential store): when firstboot runs on the live system the
           credential is resolved once and the concrete result is persisted
           here, so the word lists may be updated afterwards without changing
           the hostname. A pattern placed directly in /etc/hostname (or
           provisioned into an offline image) is instead re-evaluated on
           every boot, which only really makes sense for systems that keep
           the wordlist and the pattern stable.

           Added in version 262.

           You may use hostnamectl(1) to change the value of this file during
           runtime from the command line. Use systemd-firstboot(1) to
           initialize it on mounted (but not booted) system images.

## [](#HOSTNAME_SEMANTICS)HOSTNAME SEMANTICS

           systemd(1) and the associated tools will obtain the hostname in
           the following ways:

           •   If the kernel command line parameter systemd.hostname=
               specifies a valid hostname, systemd(1) will use it to set the
               hostname during early boot, see kernel-command-line(7),

           •   Otherwise, the "static" hostname specified by /etc/hostname as
               described above will be used.

           •   Otherwise, a transient hostname may be set during runtime, for
               example based on information in a DHCP lease, see
               systemd-hostnamed.service(8). Both NetworkManager[1] and
               systemd-networkd.service(8) allow this. Note that
               systemd-hostnamed.service(8) gives higher priority to the
               static hostname, so the transient hostname will only be used
               if the static hostname is not configured.

           •   Otherwise, a fallback hostname configured at compilation time
               will be used ("localhost").

           Effectively, the static hostname has higher priority than a
           transient hostname, which has higher priority than the fallback
           hostname. Transient hostnames are equivalent, so setting a new
           transient hostname causes the previous transient hostname to be
           forgotten. The hostname specified on the kernel command line is
           like a transient hostname, with the exception that it has higher
           priority when the machine boots. Also note that those are the
           semantics implemented by systemd tools, but other programs may
           also set the hostname.

## [](#HISTORY)HISTORY

           The simple configuration file format of /etc/hostname originates
           from Debian GNU/Linux.

## [](#SEE_ALSO)SEE ALSO

           systemd(1), sethostname(2), hostname(1), hostname(7),
           machine-id(5), machine-info(5), hostnamectl(1),
           systemd-hostnamed.service(8), systemd-firstboot(1)

## [](#NOTES)NOTES

            1. NetworkManager
               https://developer.gnome.org/NetworkManager/stable/

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

    systemd 262~devel                                             HOSTNAME(5)

------------------------------------------------------------------------

Pages that refer to this page: [hostname(1)](../man1/hostname.1.html),  [hostnamectl(1)](../man1/hostnamectl.1.html),  [systemd-firstboot(1)](../man1/systemd-firstboot.1.html),  [machine-id(5)](../man5/machine-id.5.html),  [machine-info(5)](../man5/machine-info.5.html),  [os-release(5)](../man5/os-release.5.html),  [kernel-command-line(7)](../man7/kernel-command-line.7.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd.system-credentials(7)](../man7/systemd.system-credentials.7.html),  [systemd-hostnamed.service(8)](../man8/systemd-hostnamed.service.8.html)

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
