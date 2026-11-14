---
{"title": "hwdb(7) — Linux manual page", "url": "https://man7.org/linux/man-pages/man7/hwdb.7.html", "retrieved": "2026-11-14", "license": "various (per page)"}
---

# hwdb(7) --- Linux manual page

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| [NAME](#NAME) \| [DESCRIPTION](#DESCRIPTION) \| [HARDWARE DATABASE FILES](#HARDWARE_DATABASE_FILES) \| [EXAMPLES](#EXAMPLES) \| [SEE ALSO](#SEE_ALSO) \| [COLOPHON](#COLOPHON) |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
|                                                                                                                                                                                |                                   |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

    HWDB(7)                            hwdb                           HWDB(7)

## [](#NAME)NAME

           hwdb - Hardware Database

## [](#DESCRIPTION)DESCRIPTION

           The hardware database is a key-value store for associating
           modalias-like keys to udev-property-like values. It is used
           primarily by udev to add the relevant properties to matching
           devices, but it can also be queried directly.

## [](#HARDWARE_DATABASE_FILES)HARDWARE DATABASE FILES

           The hwdb files are read from the files located in the system hwdb
           directory /usr/lib/udev/hwdb.d and the local administration
           directory /etc/udev/hwdb.d. All hwdb files are collectively sorted
           and processed in lexicographic order, regardless of the
           directories in which they live. However, files with identical
           filenames replace each other. Files in /etc/ have the highest
           priority and take precedence over files with the same name in
           /usr/lib/. This can be used to override a system-supplied hwdb
           file with a local file if needed; a symlink in /etc/ with the same
           name as a hwdb file in /usr/lib/, pointing to /dev/null, disables
           that hwdb file entirely. hwdb files must have the extension .hwdb;
           other extensions are ignored.

           Each hwdb file contains data records consisting of matches and
           associated key-value pairs. Every record in the hwdb starts with
           one or more match strings, specifying a shell glob to compare the
           lookup string against. Multiple match lines are specified in
           consecutive lines. Every match line is compared individually, and
           they are combined by OR. Every match line must start at the first
           character of the line.

           Match patterns consist of literal characters, and shell-style
           wildcards:

           •   Asterisk "*" matches any number of characters

           •   Question mark "?"  matches a single character

           •   Character list "[chars]" matches one of the characters chars
               listed between "[" and "]". A range may be specified as with a
               dash as "[first-last]". The match may be inverted with a caret
               "[^...]".

           The match lines are followed by one or more key-value pair lines,
           which are recognized by a leading space character. The key name
           and value are separated by "=". An empty line signifies the end of
           a record. Lines beginning with "#" are ignored.

           In case multiple records match a given lookup string, the
           key-value pairs from all records are combined. If a key is
           specified multiple times, the value from the record with the
           highest priority is used (each key can have only a single value).
           The priority is higher when the record is in a file that sorts
           later lexicographically, and in case of records in the same file,
           later records have higher priority.

           The content of all hwdb files is read by systemd-hwdb(8) and
           compiled to a binary database located at /etc/udev/hwdb.bin, or
           alternatively /usr/lib/udev/hwdb.bin if you want ship the compiled
           database in an immutable image. During runtime, only the binary
           database is used.

## [](#EXAMPLES)EXAMPLES

           Example 1. General syntax of hwdb files

               # /usr/lib/udev/hwdb.d/example.hwdb
               # Comments can be placed before any records. This is a good spot
               # to describe what that file is used for, what kind of properties
               # it defines, and the ordering convention.

               # A record with three matches and one property
               mouse:*:name:*Trackball*:*
               mouse:*:name:*trackball*:*
               mouse:*:name:*TrackBall*:*
                ID_INPUT_TRACKBALL=1

               # The rule above could be also be written in a form that
               # matches Tb, tb, TB, tB:
               mouse:*:name:*[tT]rack[bB]all*:*
                ID_INPUT_TRACKBALL=1

               # A record with a single match and five properties
               mouse:usb:v046dp4041:name:Logitech MX Master:*
                MOUSE_DPI=1000@166
                MOUSE_WHEEL_CLICK_ANGLE=15
                MOUSE_WHEEL_CLICK_ANGLE_HORIZONTAL=26
                MOUSE_WHEEL_CLICK_COUNT=24
                MOUSE_WHEEL_CLICK_COUNT_HORIZONTAL=14

           Example 2. Overriding of properties

               # /usr/lib/udev/hwdb.d/60-keyboard.hwdb
               evdev:atkbd:dmi:bvn*:bvr*:bd*:svnAcer*:pn*:*
                KEYBOARD_KEY_a1=help
                KEYBOARD_KEY_a2=setup
                KEYBOARD_KEY_a3=battery

               # Match vendor name "Acer" and any product name starting with "X123"
               evdev:atkbd:dmi:bvn*:bvr*:bd*:svnAcer:pnX123*:*
                KEYBOARD_KEY_a2=wlan

               # /etc/udev/hwdb.d/70-keyboard.hwdb
               # disable wlan key on all at keyboards
               evdev:atkbd:*
                KEYBOARD_KEY_a2=reserved
                PROPERTY_WITH_SPACES=some string

           If the hwdb consists of those two files, a keyboard with the
           lookup string
           "evdev:atkbd:dmi:bvnAcer:bvr:bdXXXXX:bd08/05/2010:svnAcer:pnX123:"
           will match all three records, and end up with the following
           properties:

               KEYBOARD_KEY_a1=help
               KEYBOARD_KEY_a2=reserved
               KEYBOARD_KEY_a3=battery
               PROPERTY_WITH_SPACES=some string

## [](#SEE_ALSO)SEE ALSO

           systemd-hwdb(8)

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

    systemd 262~devel                                                 HWDB(7)

------------------------------------------------------------------------

Pages that refer to this page: [sd-hwdb(3)](../man3/sd-hwdb.3.html),  [sd_hwdb_get(3)](../man3/sd_hwdb_get.3.html),  [machine-info(5)](../man5/machine-info.5.html),  [systemd.directives(7)](../man7/systemd.directives.7.html),  [systemd.index(7)](../man7/systemd.index.7.html),  [systemd-hwdb(8)](../man8/systemd-hwdb.8.html),  [systemd-imdsd@.service(8)](../man8/systemd-imdsd@.service.8.html),  [systemd-imds-generator(8)](../man8/systemd-imds-generator.8.html)

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
