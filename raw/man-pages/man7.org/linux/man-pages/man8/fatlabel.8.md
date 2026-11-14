---
{"title": "fatlabel(8) — Linux manual page", "url": "https://man7.org/linux/man-pages/man8/fatlabel.8.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# fatlabel(8) --- Linux manual page

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [SYNOPSIS](#SYNOPSIS) \| [DESCRIPTION](#DESCRIPTION) \| [OPTIONS](#OPTIONS) \| [COMPATIBILITY and BUGS](#COMPATIBILITY_and_BUGS) \| [DOS CODEPAGES](#DOS_CODEPAGES) \| [SEE ALSO](#SEE_ALSO) \| [HOMEPAGE](#HOMEPAGE) \| [AUTHORS](#AUTHORS) \| [COLOPHON](#COLOPHON) |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                                                                                                                        |                                   |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    FATLABEL(8)              System Manager's Manual              FATLABEL(8)

## [](#NAME)NAME

           fatlabel - set or get MS-DOS filesystem label or volume ID

## [](#SYNOPSIS)SYNOPSIS

           fatlabel [OPTIONS] DEVICE [NEW]

## [](#DESCRIPTION)DESCRIPTION

           fatlabel will display or change the volume label or volume ID on
           the MS-DOS filesystem located on DEVICE.  By default it works in
           label mode.  It can be switched to volume ID mode with the option
           -i or --volume-id.

           If NEW is omitted, then the existing label or volume ID is written
           to the standard output.  A label can't be longer than 11 bytes and
           should be in all upper case for best compatibility.  An empty
           string or a label consisting only of white space is not allowed.
           A volume ID must be given as a hexadecimal number (no leading "0x"
           or similar) and must fit into 32 bits.

## [](#OPTIONS)OPTIONS

           -i, --volume-id
               Switch to volume ID mode.

           -r, --reset
               Remove label in label mode or generate new ID in volume ID
               mode.

           -c PAGE, --codepage=PAGE
               Use DOS codepage PAGE to encode/decode label.  By default
               codepage 850 is used.

           -h, --help
               Display a help message and terminate.

           -V, --version
               Show version number and terminate.

## [](#COMPATIBILITY_and_BUGS)COMPATIBILITY and BUGS

           For historic reasons FAT label is stored in two different
           locations: in the boot sector and as a special volume label entry
           in the root directory.  MS-DOS 5.00, MS-DOS 6.22, MS-DOS 7.10,
           Windows 98, Windows XP and also Windows 10 read FAT label only
           from the root directory.  Absence of the volume label in the root
           directory is interpreted as empty or none label, even if boot
           sector contains some valid label.

           When Windows XP or Windows 10 system changes a FAT label it stores
           it only in the root directory — letting boot sector unchanged.
           Which leads to problems when a label is removed on Windows.  Old
           label is still stored in the boot sector but is removed from the
           root directory.

           dosfslabel prior to the version 3.0.7 operated only with FAT
           labels stored in the boot sector, completely ignoring a volume
           label in the root directory.

           dosfslabel in versions 3.0.7–3.0.15 reads FAT labels from the root
           directory and in case of absence, it fallbacks to a label stored
           in the boot sector.  Change operation resulted in updating a label
           in the boot sector and sometimes also in the root directory due to
           the bug.  That bug was fixed in dosfslabel version 3.0.16 and
           since this version dosfslabel updates label in both location.

           Since version 4.2, fatlabel reads a FAT label only from the root
           directory (like MS-DOS and Windows systems), but changes a FAT
           label in both locations.  In version 4.2 was fixed handling of
           empty labels and labels which starts with a byte 0xE5.  Also in
           this version was added support for non-ASCII labels according to
           the specified DOS codepage and were added checks if a new label is
           valid.

           It is strongly suggested to not use dosfslabel prior to version
           3.0.16.

## [](#DOS_CODEPAGES)DOS CODEPAGES

           MS-DOS and Windows systems use DOS (OEM) codepage for encoding and
           decoding FAT label.  In Windows systems DOS codepage is global for
           all running applications and cannot be configured explicitly.  It
           is set implicitly by option Language for non-Unicode programs
           available in Regional and Language Options via Control Panel.
           Default DOS codepage for fatlabel is 850.  See following mapping
           table between DOS codepage and Language for non-Unicode programs:
           Codepage   Language
             437      English (India), English (Malaysia), English (Republic
                      of the Philippines), English (Singapore), English
                      (South Africa), English (United States), English
                      (Zimbabwe), Filipino, Hausa, Igbo, Inuktitut,
                      Kinyarwanda, Kiswahili, Yoruba
             720      Arabic, Dari, Persian, Urdu, Uyghur
             737      Greek
             775      Estonian, Latvian, Lithuanian
             850      Afrikaans, Alsatian, Basque, Breton, Catalan, Corsican,
                      Danish, Dutch, English (Australia), English (Belize),
                      English (Canada), English (Caribbean), English
                      (Ireland), English (Jamaica), English (New Zealand),
                      English (Trinidad and Tobago), English (United
                      Kingdom), Faroese, Finnish, French, Frisian, Galician,
                      German, Greenlandic, Icelandic, Indonesian, Irish,
                      isiXhosa, isiZulu, Italian, K'iche, Lower Sorbian,
                      Luxembourgish, Malay, Mapudungun, Mohawk, Norwegian,
                      Occitan, Portuguese, Quechua, Romansh, Sami, Scottish
                      Gaelic, Sesotho sa Leboa, Setswana, Spanish, Swedish,
                      Tamazight, Upper Sorbian, Welsh, Wolof
             852      Albanian, Bosnian (Latin), Croatian, Czech, Hungarian,
                      Polish, Romanian, Serbian (Latin), Slovak, Slovenian,
                      Turkmen
             855      Bosnian (Cyrillic), Serbian (Cyrillic)
             857      Azeri (Latin), Turkish, Uzbek (Latin)
             862      Hebrew
             866      Azeri (Cyrillic), Bashkir, Belarusian, Bulgarian,
                      Kyrgyz, Macedonian, Mongolian, Russian, Tajik, Tatar,
                      Ukrainian, Uzbek (Cyrillic), Yakut
             874      Thai
             932      Japanese
             936      Chinese (Simplified)
             949      Korean
             950      Chinese (Traditional)
             1258     Vietnamese

## [](#SEE_ALSO)SEE ALSO

           fsck.fat(8), mkfs.fat(8)

## [](#HOMEPAGE)HOMEPAGE

           The home for the dosfstools project is its GitHub project page 
           ⟨https://github.com/dosfstools/dosfstools⟩.

## [](#AUTHORS)AUTHORS

           dosfstools were written by Werner Almesberger ⟨werner.almesberger@
           lrc.di.epfl.ch⟩, Roman Hodek ⟨Roman.Hodek@informatik.uni-
           erlangen.de⟩, and others.  Current maintainers are Andreas Bombe
           ⟨aeb@debian.org⟩ and Pali Rohár ⟨pali.rohar@gmail.com⟩.

## [](#COLOPHON)COLOPHON

           This page is part of the dosfstools (Tools for making and checking
           MS-DOS FAT filesystems) project.  Information about the project
           can be found at ⟨https://github.com/dosfstools/dosfstools⟩.  If
           you have a bug report for this manual page, see
           ⟨https://github.com/dosfstools/dosfstools/issues⟩.  This page was
           obtained from the project's upstream Git repository
           ⟨https://github.com/dosfstools/dosfstools.git⟩ on 2026-08-03.  (At
           that time, the date of the most recent commit that was found in
           the repository was 2023-10-10.)  If you discover any rendering
           problems in this HTML version of the page, or you believe there is
           a better or more up-to-date source for the page, or you have
           corrections or improvements to the information in this COLOPHON
           (which is not part of the original manual page), send a mail to
           man-pages@man7.org

    dosfstools 4.2+git              2021-01-31                    FATLABEL(8)

------------------------------------------------------------------------

Pages that refer to this page: [fstab(5)](../man5/fstab.5.html),  [dosfsck(8)](../man8/dosfsck.8.html),  [fsck.fat(8)](../man8/fsck.fat.8.html),  [fsck.msdos(8)](../man8/fsck.msdos.8.html),  [fsck.vfat(8)](../man8/fsck.vfat.8.html),  [mkdosfs(8)](../man8/mkdosfs.8.html),  [mkfs.fat(8)](../man8/mkfs.fat.8.html),  [mkfs.msdos(8)](../man8/mkfs.msdos.8.html),  [mkfs.vfat(8)](../man8/mkfs.vfat.8.html)

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
